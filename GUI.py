from tkinter import *  
from tkinter.ttk import *
import matplotlib.pyplot as plt
# import GetData
# dsa=GetData.gett()
root = Tk()  

label = Label(text="股票代码")
label.grid(row=0,column=0)
starttimeinput7 = Combobox(width=10)
starttimeinput7.grid(row=0,column=1) 

starttime=Label(text="开始时间")
starttime.grid(row=2,column=0)
starttimeinput = Combobox( values=["2015", "2016", "2017","2018"],width=10)
starttimeinput.grid(row=2,column=1) 

starttimeinput1=Combobox(values=["01", "02","03","04","05","06","07","08","09","10","11","12"],width=10)
starttimeinput1.grid(row=2,column=2) 

starttimeinput2 = Combobox(values=["01", "02","03","04","05","06","07","08","09","10","11","12","13", "14", "15","16","17", "18","19","20","21","22","23","24","25","26","27","28","29", "30", "31"],width=10)
starttimeinput2.grid(row=2,column=3) 
##结束时间
starttime1=Label(text="结束时间")
starttime1.grid(row=3,column=0)
starttimeinput3 = Combobox(values=["2015", "2016", "2017","2018"],width=10)
starttimeinput3.grid(row=3,column=1) 

starttimeinput4=Combobox(values=["01", "02","03","04","05","06","07","08","09","10","11","12"],width=10)
starttimeinput4.grid(row=3,column=2) 

starttimeinput5 = Combobox(values=["01", "02","03","04","05","06","07","08","09","10","11","12","13", "14", "15","16","17", "18","19","20","21","22","23","24","25","26","27","28","29", "30", "31"],width=10)
starttimeinput5.grid(row=3,column=3) 
labelm =Label(text="买入价格")
labelm.grid(row=5,column=0)
entrym =Entry()#输入框
entrym.grid(row=5,column=1)

label2=Label(text="交易设置：高于买入价%")#设置交易条件
label2.grid(row=6)
gsetup = Combobox(root, values=["5", "6", "7","8","9","10"],width=10)
gsetup.grid(row=6,column=1) 

# w1 = Combobox(root,  values=["5", "6", "7","8","9","10"],width=10)
# w1.grid(row=2,column=1)

label4=Label(text="交易次数")#设置交易次数
label4.grid(row=6,column=2)
gnumber = Combobox(root,values=["1", "2", "3","4","5","6"],width=10)
gnumber.grid(row=6,column=3)
# w1 = Combobox(root, values=["1", "2", "3","4","5","6"],width=10)
# w1.grid(row=2,column=3)

label5=Label(text="交易设置：低于买入价%")#设置交易条件
label5.grid(row=8)

dsetup = Combobox(root, values=["5", "6", "7","8","9","10"],width=10)
dsetup.grid(row=8,column=1)

label6=Label(text="交易次数")#设置交易次数
label6.grid(row=8,column=2)
gnumber = Combobox(root,values=["1", "2", "3","4","5","6"],width=10)
gnumber.grid(row=8,column=3)


button2=Button(root,text="黄金买点")#,command=prints
button2.grid(row=4,column=1)


dnumber = Combobox(root,values=["1", "2", "3","4","5","6"],width=10)
dnumber.grid(row=3,column=3)

label3=Label(text="交易结果")
label3.grid(row=5)


button=Button(root,text="绘制K线图")##,command=gett
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

tg=Label(text="RSI小于")
tg.grid(row=10)
# rsid = Combobox(root, values=["大于","小于"],width=10)
# rsid.grid(row=10,column=1)
rsi=Combobox(root, values=["10", "20", "25","30"],width=10)
rsi.grid(row=10,column=2)

tg1=Label(text="DMA小于")
tg1.grid(row=12)
# dmad = Combobox(root, values=["大于","小于"],width=10)
# dmad.grid(row=12,column=1)
dma = Combobox(root, values=["-1", "-2", "-3"],width=10)
dma.grid(row=12,column=2)

tg2=Label(text="BIAS小于")
tg2.grid(row=14)
# biasd = Combobox(root, values=["大于","小于"],width=10)
# biasd.grid(row=14,column=1)
bias = Combobox(root, values=["-10", "-12", "-11","-9","-18"],width=10)
bias.grid(row=14,column=2)

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
buttonrsi=Button(root,text="查询")#,command=RMD
buttonrsi.grid(row=20)



radiobutton=Radiobutton(root,text="3333")
root.mainloop()

#获取输入框内数据
	# aa=starttimeinput7.get()
	# ##开始时间
	# t=starttimeinput.get()#年
	# i=starttimeinput1.get()#月
	# m=starttimeinput2.get()#日
	# statime=t+"-"+i+"-"+m
	# ##结束时间
	# e=starttimeinput3.get()#年
	# n=starttimeinput4.get()#月
	# d=starttimeinput5.get()#日
	# endtime=e+"-"+n+"-"+d