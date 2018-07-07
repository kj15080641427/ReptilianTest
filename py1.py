# #最高价高于买入价8%时，卖出股票100股，交易一次
# for x in highArr:
# 	if (x-buyprice)/buyprice>0.08:  
# 		print("最高价高于买入价8%卖出股票100股，交易一次")
# 		break

# #最高价高于买入价5%时，卖出股票100股，交易一次
# for x in highArr:
# 	if (x-buyprice)/buyprice>0.05and(x-buyprice)/buyprice<0.08:
# 		print("最高价高于买入价5%卖出股票100股，交易一次")
# 		break

# #最低价低于买入价8%卖出股票100股，交易一次
# for x in lowArr:
# 	if (buyprice-x)/buyprice>0.08:
# 		print("最低价低于买入价8%买入股票100股，交易一次")
# 		break
# 	#最低价不低于8%时

# #最低价低于买入价5%卖出股票100股，交易一次
# for x in lowArr:
# 	if (buyprice-x)/buyprice>0.05and(buyprice-x)/buyprice<0.08:
# 		print("最低价低于买入价5%买入股票100股，交易一次")
# 		break
# 	else:
# 		print("无")
# sum=0
# for x in range(1,101):
# 	if x%2==0:
# 		continue
# 	print(x)





# 

# def gett():
# 	pass
from pandas import DataFrame, Series
import pandas as pd; import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates as mdates
from matplotlib import ticker as mticker
from mpl_finance import candlestick_ohlc
from tkinter import *  
from tkinter.ttk import *
from WindPy import *
from datetime import datetime
from matplotlib.dates import DateFormatter

import Reptilian#####my module


from  tkinter import ttk
import tkinter as tk

# Reptilian.main()
root = Tk()  

label =Label(text="股票代码")
label.grid(row=0,column=0)
starttimeinput7 = Combobox(values=['000001.SZ','600000.SH'],width=10)
starttimeinput7.grid(row=0,column=1) 
starttimeinput7.current(0) 

starttime=Label(text="开始时间")
starttime.grid(row=1,column=0)
starttimeinput = Combobox( values=["2015", "2016", "2017","2018"],width=10)
starttimeinput.grid(row=1,column=1) 
starttimeinput.current(3) 

starttimeinput1=Combobox(values=["01", "02","03","04","05","06","07","08","09","10","11","12"],width=10)
starttimeinput1.grid(row=1,column=2) 
starttimeinput1.current(0) 

starttimeinput2 = Combobox(values=["01", "02","03","04","05","06","07","08","09","10","11","12","13", "14", "15","16","17", "18","19","20","21","22","23","24","25","26","27","28","29", "30", "31"],width=10)
starttimeinput2.grid(row=1,column=3) 
starttimeinput2.current(0) 
##结束时间
starttime1=Label(text="结束时间")
starttime1.grid(row=3,column=0)
starttimeinput3 = Combobox(values=["2015", "2016", "2017","2018"],width=10)
starttimeinput3.grid(row=3,column=1) 
starttimeinput3.current(3) 

starttimeinput4=Combobox(values=["01", "02","03","04","05","06","07","08","09","10","11","12"],width=10)
starttimeinput4.grid(row=3,column=2) 
starttimeinput4.current(1) 

starttimeinput5 = Combobox(values=["01", "02","03","04","05","06","07","08","09","10","11","12","13", "14", "15","16","17", "18","19","20","21","22","23","24","25","26","27","28","29", "30", "31"],width=10)
starttimeinput5.grid(row=3,column=3) 
starttimeinput5.current(0) 

# labelm =Label(text="买入价格")
# labelm.grid(row=5,column=0)
# entrym =Entry()#输入框
# entrym.grid(row=5,column=1)

# label2=Label(text="交易设置：高于买入价%")#设置交易条件
# label2.grid(row=6)
# gsetup = Combobox(root, values=["5", "6", "7","8","9","10"],width=10)
# gsetup.grid(row=6,column=1) 

# w1 = Combobox(root,  values=["5", "6", "7","8","9","10"],width=10)
# w1.grid(row=2,column=1)

# label4=Label(text="交易次数")#设置交易次数
# label4.grid(row=6,column=2)
# gnumber = Combobox(root,values=["1", "2", "3","4","5","6"],width=10)
# gnumber.grid(row=6,column=3)
# # w1 = Combobox(root, values=["1", "2", "3","4","5","6"],width=10)
# # w1.grid(row=2,column=3)

# label5=Label(text="交易设置：低于买入价%")#设置交易条件
# label5.grid(row=8)

# dsetup = Combobox(root, values=["5", "6", "7","8","9","10"],width=10)
# dsetup.grid(row=8,column=1)

# label6=Label(text="交易次数")#设置交易次数
# label6.grid(row=8,column=2)
# gnumber1 = Combobox(root,values=["1", "2", "3","4","5","6"],width=10)
# gnumber1.grid(row=8,column=3)

# w3 = Combobox(root,  values=["5", "6", "7","8","9","10"],width=10)427.85
# w3.grid(row=9,column=1)


# def prints():
# 	w.start()
# 	data=w.wsd("000002.SZ","close,high,low","2018-01-15","2018-03-07","Fill=Previous")
# 	#print(data)
# 	# close_data=[]
# 	# for x in data.Data[0]:
# 	# 	close_data.append(x)  #将最高价数据添加到数组中
# 	print(data.Data[0])  #
# 	print(len(data.Data[0]))
# 	numa=[]
# 	numb=[]#12日diff值数组
# 	diff=[]
# 	dif=0
# 	i=0


# 	#EMA12日
# 	i=0
# 	for x in range(len(data.Data[0])):
# 		if i<1:
# 			EMA=data.Data[0][0]
# 			numa.append(EMA)
# 			i=i+2
# 		else:
# 			EMA=2*data.Data[0][x]/(13)+(11)*numa[x-1]/(13)
# 			numa.append(EMA)
# 			EMA=0
# 	print("12日EMA值：",numa)
# 	###EMA26日
# 	j=0
# 	for x in range(len(data.Data[0])):
# 		if j<1:
# 			EMA2=data.Data[0][0]
# 			numb.append(EMA2)
# 			j=j+2
# 		else:
# 			EMA2=2*data.Data[0][x]/(27)+(25)*numb[x-1]/(27)
# 			numb.append(EMA2)
# 			EMA2=0
# 	#print("26日EMA值：",numb)

# 	###DIFF值
# 	for x in range(len(data.Data[0])):
# 		dif=numa[x]-numb[x]
# 		diff.append(dif)
# 		dif=0
# 	#print("DIFF值：",diff)


# 	##	# #DEA指数
# 	deanum=0
# 	DEA=[]
# 	k=0
# 	for x in range(len(diff)):
# 		if k<1:
# 			deanum=diff[0]
# 			DEA.append(deanum)
# 			k=k+2
# 		else:
# 			deanum=2*diff[x]/(10)+(8)*DEA[x-1]/(10)
# 			DEA.append(deanum)
# 			deanum=0
# 	#print("DEA值：",DEA)

# 	##A1赋值：上次一日前DIFF上穿DEA距今天数
# 	time=[]
# 	for x in range(len(diff)):
# 		if diff[x]>DEA[x] and diff[x-1]<DEA[x-1]:
# 			time.append(x)
# 	print(time)

# 	aa=time[-1]
# 	cd=len(data.Data[0])-time[-1]
# 	print("距今天数",cd)
# 	print("DIFF上穿DEA距今最近日期",data.Times[aa])

# 	##B1赋值
# 	# for x in range(len(data.Times)):
# 	# print(data.Data[0][aa])
# 	# print(data.Data[0][-1])
# 	if data.Data[0][time[-1]-1]>data.Data[0][-1] and diff[time[-1]-1]<diff[-1] and diff[-1]>DEA[-1]:
# 			print("黄金买点",data.Times[-1])
# 	print(data.Times[-1])
		


# 	##KDJ赋值：
# 	l=0
# 	b1=0
# 	bnum=[]
# 	bnum2=[]
# 	rsv=0
# 	rsvnum=[]
# 	for x in range(len(data.Data[0])):
# 			b1=data.Data[2][x]
# 			b2=data.Data[1][x]
# 			bnum.append((b1))
# 			bnum2.append((b2))
# 			minx=min(bnum)
# 			maxx=max(bnum2)
# 			l=l+1
# 			rsv=(data.Data[0][x]-minx)/(maxx-minx)*100
# 			rsvnum.append("%.2f" %rsv)
# 			#print(len(bnum2))
# 			if l>8:
# 				#print("最低价",bnum)
# 				#print("最高价",bnum2)
# 				bnum.pop(0)
# 				bnum2.pop(0)
# 	print(rsvnum)

# 			# K值=2/3×第8日K值+1/3×第9日RSV
# 			# D值=2/3×第8日D值+1/3×第9日K值
# 			# J值=3*第9日K值-2*第9日D值
# 	##计算K值
# 	k=0
# 	knum=[]
# 	for x in range(len(rsvnum)):
# 		if x==0:
# 			k=2/3*50+1/3*float(rsvnum[x])
# 			knum.append(k)
# 			k=0
# 		else:
# 			k=2/3*float(knum[x-1])+1/3*float(rsvnum[x])
# 			knum.append(k)
# 			k=0
# 	print("K值为：",knum)
# 	##计算D 值
# 	d=0
# 	dnum=[]
# 	for x in range(len(rsvnum)):
# 		if x==0:
# 			d=2/3*50+1/3*float(rsvnum[x])
# 			dnum.append(d)
# 			d=0
# 		else:
# 			d=2/3*float(dnum[x-1])+1/3*float(knum[x])
# 			dnum.append(d)
# 			d=0
# 	print("D值",dnum)


# 	##上次KDJ的K值上穿KDJ的D值距今最近日期
# 	timekdj=[]
# 	for x in range(len(rsvnum)):
# 		if knum[x]>dnum[x] and knum[x-1]<dnum[x-1]:
# 			timekdj.append(x)
# 	kdj=timekdj[-1]
# 	print("上次KDJ的K值上穿KDJ的D值距今最近日期",data.Times[kdj])
# 	print(timekdj)

# 	print(data.Data[0][timekdj[-1]-1])
# 	print(data.Data[0][-1])
# 	if data.Data[0][timekdj[-1]-1]>data.Data[0][-1] and knum[timekdj[-1]-1]<knum[-1] and knum[-1]>dnum[-1]:
# 		print("黄金买点")




# 	# 折线图
# 	y1=diff
# 	x1=data.Times
# 	x2=data.Times
# 	y2=DEA
# 	plt.plot(x1,y1,label='DIFF值',color='b',  
# 	markerfacecolor='blue',markersize=12) 
# 	plt.plot(x2,y2,label='DEA值',color="y")
# 	plt.xlabel('Time') 
# 	plt.ylabel('Important var') 
# 	plt.title('Interesting Graph\nCheck it out') 
# 	plt.legend() 
# 	plt.show() ##button(黄金买点)

# button2=Button(root,text="黄金买点",command=prints)
# button2.grid(row=4,column=1)
###绘制K线图
def gett():#button(确定)
	#股票代码
	aa=starttimeinput7.get()
	##开始时间
	t=starttimeinput.get()#年
	i=starttimeinput1.get()#月
	m=starttimeinput2.get()#日
	statime=t+"-"+i+"-"+m
	##结束时间
	e=starttimeinput3.get()#年
	n=starttimeinput4.get()#月
	d=starttimeinput5.get()#日
	endtime=e+"-"+n+"-"+d
	if len(statime)<9 or len(endtime)<10 or len(aa)<8:
		print("不能为空")
		print(len(statime))
		print(len(endtime))
		print(len(aa))
	else:
		w.start()
		plt.rcParams['font.sans-serif'] = ['SimHei']
		plt.rcParams['axes.unicode_minus'] = False
		dailyQuota=w.wsd(aa, "open,high,low,close",statime,endtime, "Fill=Previous")
		# print(dailyQuota.Times)
		# print(len(dailyQuota.Data))
		tupleQuota=[]
		for i in range(len(dailyQuota.Data[0])):
		    tupleQuota.append((dailyQuota.Times[i].toordinal(),dailyQuota.Data[0][i],dailyQuota.Data[1][i],dailyQuota.Data[2][i],dailyQuota.Data[3][i]))
		print(tupleQuota)
		mondayFormatter = DateFormatter('%Y-%m-%d') 
		fig, ax = plt.subplots()
		ax.xaxis.set_major_formatter(mondayFormatter)
		candlestick_ohlc(ax,tupleQuota, width=0.4, colorup='r', colordown='g')
		plt.xticks(rotation=30)
		plt.title(aa)
		plt.show()





aaa=datetime.today()
# aaa='2018-04-24'


button=Button(root,text="绘制K线图",command=gett)
button.grid(row=4)

xhx=Label(text="------------------------")
xhx.grid(row=9,column=0)
xhx=Label(text="------------------------")
xhx.grid(row=9,column=1)
xhx=Label(text="------------------------")
xhx.grid(row=9,column=2)
xhx=Label(text="------------------------")
xhx.grid(row=9,column=3)
xhx=Label(text="------------------------")
xhx.grid(row=9,column=4)

chartg = tk.IntVar()
tg=tk.Checkbutton(root, text='RSI')
tg.grid(row=10)
tg.select() 
# rsid = Combobox(root, values=["大于","小于"],width=10)
# rsid.grid(row=10,column=1)
rsi=Combobox(root, values=["10", "20", "25","30","自选"],width=10)
rsi.grid(row=10,column=2)
rsi.current(0) 

chartg1 = tk.IntVar()
tg1=tk.Checkbutton(root, text='DMA')
tg1.grid(row=12)
tg1.select()
# dmad = Combobox(root, values=["大于","小于"],width=10)
# dmad.grid(row=12,column=1)
dma = Combobox(root, values=["-1", "-2", "-3","自选"],width=10)
dma.grid(row=12,column=2)
dma.current(0) 

chartg2 = tk.IntVar()
tg2=tk.Checkbutton(root, text='BIAS')
tg2.grid(row=14)
tg2.select()
# biasd = Combobox(root, values=["大于","小于"],width=10)
# biasd.grid(row=14,column=1)
bias = Combobox(root, values=["-10", "-12", "-11","-9","-18","自选"],width=10)
bias.grid(row=14,column=2)
bias.current(0) 

chartg3 = tk.IntVar()
tg3 = tk.Checkbutton(root,text='净利率')
tg3.grid(row=15)
tg3.select()

jll = Combobox(root,values=['5','10','15','20'],width=10)
jll.grid(row=15,column=2)
jll.current(0)


num=[]
# print(data)
numname=[]
xnum=[]
numto=[]
dfnum=[]
twonum=[]
numberrsi=[]
numberdma=[]
numberbias=[]
stock_code1=[]
# print(data.Codes)
w.start()

AllAStock=w.wset("SectorConstituent",u"date=20180101;sector=全部A股") 
#把股票代码转变为列表格式  
stock_code=AllAStock.Data[1]

zidian=Reptilian.main()

setdaima = set(zidian[0])
for x in range(len(stock_code)):
	df=stock_code[x].split('.')[0]
	dfnum.append(df)
set2stock = set(dfnum)
allnum=set2stock & setdaima
# print ('哇哇哇',allnum)

for x in allnum:
	twonum.append(x)##两组数据相同的股票代码
# print(twonum[0])
# print(stock_code[0])
for x in range(len(stock_code)):
	if stock_code[x].split('.')[0] in twonum:
		xnum.append(x)###下标
# print(xnum)

for x in xnum:
	stock_code1.append(stock_code[x])
# print(stock_code1[1])####rsi，dma,bias代码新数组


data=w.wsd(stock_code1,"rsi",aaa,aaa,"Fill=Previous")###获取RSI值
data1=w.wsd(stock_code1,"dma",aaa,aaa,"Fill=Previous")#DMA
data2=w.wsd(stock_code1,"bias",aaa,aaa,"Fill=Previous")#BIAS
lengh=len(data.Data[0])
for x in range(lengh):
		numberrsi.append(data.Data[0][x])#RSI  将rsi添加到numberrsi
		numberdma.append(data1.Data[0][x])##DMA
		numberbias.append(data2.Data[0][x])##BIAS
def RMD():
	num=[]
	numto=[]

	sizersi=float(rsi.get())
	sizedma=float(dma.get())
	sizebias=float(bias.get())
	sizejll=float(jll.get())
	# print(sizersi)

	for x in range(lengh):
		if sizersi =="" :
	 		print("不能为空")
		elif numberrsi[x]<sizersi and  numberdma[x]<sizedma and numberbias[x]<sizebias :
			# if stock_code[x] not in num:
			# jll=float(num.split('.')[0])
			num.append(stock_code1[x])
			numname.append(AllAStock.Data[2][x]) 

	# print('符合条件的股票',num)

	for x in range(len(num)):
		ass=num[x].split('.')[0].split()
		numto.append(ass)
	# print(numto)
	# print('字典',zidian[1])
	# print(zidian[numto[0]])
	# print(jllnum)
	for x in range(len(numto)):
		dx=numto[x]
		# print('字典',dx[0])
		cx=zidian[1][dx[0]].split('%')[0]
		if float(cx)>sizejll:
			tree.insert("",0,values=(numto[x],cx)) #插入数据,  
			print(cx)
	num=[]
	numto=[]


def dell():
	items = tree.get_children()
	[tree.delete(item) for item in items]

buttonrsi=Button(root,text="查询",command=RMD)
buttonrsi.grid(row=16)

buttonrdel=Button(root,text="清屏",command=dell)
buttonrdel.grid(row=17)

tree=ttk.Treeview(root,show='headings')#表格  
tree["columns"]=("名称","净利率")  
tree.column("名称",width=100)   #表示列,不显示  
tree.column("净利率",width=100)    
  
tree.heading("名称",text="-名称-")  #显示表头  
tree.heading("净利率",text="-净利率-")  


tree.grid(row=17,column=2)  

radiobutton=Radiobutton(root,text="3333")
root.mainloop()



