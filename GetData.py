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
# import Reptilian#####my module


class Data(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.gett 
		
	###绘制K线图
	def gett():#button(确定)
	#股票代码

		w.start()
		plt.rcParams['font.sans-serif'] = ['SimHei']
		plt.rcParams['axes.unicode_minus'] = False
		dailyQuota=w.wsd(aa, "open,high,low,close",statime,endtime, "Fill=Previous")
		print(dailyQuota.Times)
		print(len(dailyQuota.Data))
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


	##获取RSI DMA BIAS
	def RMD():
		aaa=datetime.today()
		num=[]
		w.start()

		AllAStock=w.wset("SectorConstituent",u"date=20130608;sector=全部A股") 
		#把股票代码转变为列表格式  
		stock_code=AllAStock.Data[1]    
		# print(AllAStock.Data[1])

		data=w.wsd(stock_code,"rsi",aaa,aaa,"Fill=Previous")###获取RSI值
		data1=w.wsd(stock_code,"dma",aaa,aaa,"Fill=Previous")#DMA
		data2=w.wsd(stock_code,"bias",aaa,aaa,"Fill=Previous")#BIAS
		# print(data)

		numberrsi=[]
		numberdma=[]
		numberbias=[]

		lengh=len(data1.Data[0])

		for x in range(lengh):
				numberrsi.append(float('%.2f'%data.Data[0][x]))#RSI  将rsi添加到numberrsi
				numberdma.append(float('%.2f'%data1.Data[0][x]))##DMA
				numberbias.append(float('%.2f'%data2.Data[0][x]))##BIAS
		# print(number)

		sizersi=rsi.get()#####获取输入框内容
		sizedma=dma.get()
		sizebias=bias.get()
		print(sizebias)
		print(sizersi)

c=Data
	# rsitxt=rsid.get()
	# dmatxt=dmad.get()
	# biastxt=biasd.get()

	# if rsitxt="小于":
	

	# for x in range(lengh):
	# 	if sizersi =="" :
	#  		print("不能为空")
	# 	elif numberrsi[x]<sizersi and  numberdma[x]<sizedma and numberbias[x]<sizebias:
	#  		num.append(stock_code[x])
	# print(num)






