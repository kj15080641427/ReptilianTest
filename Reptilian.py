#-*-coding:utf-8-*-
#2097

#############
import requests,re,json,time,os
import heapq

import xlsxwriter
import xlrd
from xlwt import *  

from bs4 import BeautifulSoup

class GPINFO(object):
	"""docstring for GPINFO"""
	def __init__(self):
		self.Url = 'http://quote.eastmoney.com/stocklist.html'
		self.BaseData = []
		self.Date = time.strftime('%Y%m%d')
		self.Record = 'basedata'
		if os.path.exists(self.Record):
			print ('record exist...\n')
			self.BaseData = self.get_base_data_from_record()
			# self.write_excel(self.BaseData)
			# print(self.BaseData)
		else:
			print ('get data again...')
			self.get_data()

	##写入到Excel
	# def write_excel(self,txt ):
	# 	file = Workbook(encoding = 'utf-8')  
	# 	#指定file以utf-8的格式打开  
	# 	table = file.add_sheet('cccccccccccc')  
	# 	#指定打开的文件名  

	# 	# print("EXCEL",txt)
	# 	num=[]
	# 	for x in txt:
	# 		num.append(x)
	# 	# print(num[0]['名称'])
	# 	# print(len(num))
	# 	print(num)
	# 	for x in num:  
	# #for循环将data字典中的键和值分批的保存在ldata中  
	# 		t = (x)  
	# 		print(t)
	# 	for j in range(len(num)):  
	# 		table.write(num[j]['名称']) 


	# 		for a in num[x]:  
	# 			# print(a)
	# 			t.append(a)  
	# 			ldata.append(t) 



    #将数据写入到记录文件
	def write_record(self,text):
		with open(self.Record,'ab') as f:
			f.write((text+'\n').encode("utf-8"))

    #从记录文件从读取数据
	def get_base_data_from_record(self):
		ll = []
		with open(self.Record,'rb') as f:
			json_l = f.readlines()
			for j in json_l:
				ll.append(json.loads(j.decode("utf-8")))
		return ll
    #爬虫获取数据
	def get_data(self):
		#请求数据
		orihtml = requests.get(self.Url).content
		#创建 beautifulsoup 对象
		soup = BeautifulSoup(orihtml,'lxml')
		#采集每一个股票的信息
		count = 0
		for a in soup.find('div',class_='quotebody').find_all('a',{'target':'_blank'}):
			record_d = {}##创建字典
			#代号
			num = a.get_text().split('(')[1].strip(')')  #获取股票代号  split('(')以'('分割为两段 并只取[1] ( '(' 后的数据)  .strip(')') 为删除右括号   东方财富网站股票名称代码格式为  万科A(000002)

			if not (num.startswith('00') or num.startswith('60')):continue #只需要6*/0*    只要以00或60开头的股票代号
			record_d['股票代码']=num	##创建字典 键为:num  值为:股票代码

			#名称
			name = a.get_text().split('(')[0] 	 #获取股票名称   以'('分割  并只取'('前的数据。   万科A(000002)
			record_d['名称']=name 	##创建字典 键为：name。值为：股票名称

			#详情页
			detail_url = a['href']	##获取a的href链接
			# record_d['detail_url']=detail_url

			cwzburl = detail_url ##将获取到的链接赋值给cwzburl

            #发送请求
			try:
				cwzbhtml = requests.get(cwzburl,timeout=50).content #爬取股票详情页  30秒内无反应则抛出错误
			except Exception as e:
				print ('perhaps timeout:',e)	#打印错误信息
				continue   ##跳出此次循环

            #创建soup对象
			cwzbsoup = BeautifulSoup(cwzbhtml,'lxml')

			try:
				cwzb_list = cwzbsoup.find('div',class_='cwzb').tbody.tr.get_text().split()  #获取class为cwzb的div下第一个tbody下第一个tr获取内部文本，并使用空格分割
				# cwzb_list = cwzbsoup.find('ul',class_='_technologyindex').li.get_text().split()
			except Exception as e:
				print ('error:',e)
				continue
				# /html/body/div[1]/div[13]/div[2]/div[2]/div[2]/div[6]/table/tbody/tr[1]/td[7]
            #去除退市股票
			if '-' not in cwzb_list:
				record_d['净利率']=cwzb_list   #将数据加入到字典中
				self.BaseData.append(record_d)  #将字典加入到总数据总
				self.write_record(json.dumps(record_d))  #将字典类型转化为字符串，写入文本
				count=count+1
				print (len(self.BaseData))

def main():
	daimanum=[]
	jllnum=[]
	zidian={}
	test = GPINFO()
	# test.get_base_data_from_record()
	result = test.BaseData
	# print(result)
	# for x in range(len(result)):
	# 	jll=float(result[x]['净利率'].split('%')[0])
		# jllnum.append(jll)
		# if jll>10:
		# 	print(result[x])
	# return jllnum
	for x in range(len(result)):
		daimanum.append(result[x]['股票代码'])
		jllnum.append(result[x]['净利率'])
	# print(jllnum)
	# print(daimanum)
	for x in range(len(jllnum)):
		zidian[daimanum[x]]=jllnum[x]
	# print(daimanum)
	# print(zidian)
	# return daimanum,zidian


	# print(len(jllnum))

	# #[浦发银行，总市值    净资产    净利润    市盈率    市净率    毛利率    净利率    ROE] roe:净资产收益率]
	# top_10 = heapq.nlargest(10,result,key=lambda r:float(r['data'][7].strip('%')))   #获取前10名利率最高者的数据
	# for item in top_10:
	# 	for key in item['data']:
	#     print(key),
	# print('\n')

	# 打印字符串时，使用print str.encode('utf8');
	# 打印中文列表时，使用循环 for key in list：print key
	# 打印中文字典时，可以使用循环，也可以使用json：
	#  import json
	# print json.dumps(dict, encoding='UTF-8', ensure_ascii=False)


if __name__ == '__main__':
	main()




    # //*[@id="QuestionAnswers-answers"]/div/div/div[2]/div/div[5]/div/div[2]/div[1]/span/p[29]