##coding:utf-8
#折线图/散点图 plot
import matplotlib.pylab as pyl
import numpy as npy
x=[1,2,3,4,8]
y=[5,7,2,1,5]

#pyl.plot(x,y) #plot(X轴数据，Y轴数据，展现形式)
#pyl.plot(x,y,'o')
#pyl.plot(x,y,'oy')
#pyl.plot(x,y,'r')
#pyl.show()
'''
c-cyan --青色
r-red
m-magente-品红
g-green
b-blue
y-yellow
k-black
w-white

'''
#线条样式
'''
- 直线
--虚线
-.  -.形式
: 细小虚线

'''
#pyl.plot(x,y,'--')
#pyl.plot(x,y,'-.')
#pyl.plot(x,y,':')
#pyl.show()
#点的样式
'''
s --方形
h --六角形
H --六角形
*--
+
x
d--菱形
D--菱形
p--五角形
'''
#pyl.plot(x,y,'*')
#pyl.plot(x,y,'-D')

x2=[1,3,6,8,10,12,19]
y2=[1,6,9,10,19,23,25]
'''
pyl.plot(x2,y2)

pyl.title("show")
pyl.xlabel("ages")
pyl.ylabel("y轴数据")
pyl.xlim(0,10)  #限制x显示范围
pyl.ylim(0,8)   #限制y显示范围
pyl.show()
'''
#随机数
'''
import numpy as npy
data=npy.random.random_integers(1,50,5)#(最小值，最大值,个数)

#直方图hist
data2=npy.random.normal(10.0,1.0,10000)#(均数，西格玛，个数)
#print(data2)
#pyl.hist(data2)
#pyl.show()
pyl.subplot(2,2,1)#行，列，当前区域,指定图形展示区域
pyl.plot(x2,y2)

pyl.subplot(2,1,2)
pyl.plot(x,y)

x3=[1,2,3,4,5,6]
y3=[2,4,6,8,9,10]
pyl.subplot(2,2,2)
pyl.plot(x3,y3)

pyl.show()
'''
#读取文件内容，并展示

import pandas as pda
import numpy as npy
import matplotlib.pylab as pyl
data = pda.read_csv("C:/Users/joe/PycharmProjects/GetHotspot/test.csv", encoding='ISO-8859-1', sep=',', header=None)
#data.values() #[行][列]
data2 = data.T #行列转换
data.shape
data.values[1][1]
x1 = data2.values[0]
y1 = data2.values[1]
#pyl.plot(x1,y1,"H")
#pyl.show()

#数据清洗
#发现缺失值
'''
print(data.describe())
print(len(data))
x=0
for i in data.columns:
    for j in range(len(data)):
        if(data[i].isnull())[j]:
            data[i][j]="35"
            x+=1
print(x)
'''
#异常值处理
#画散点图
data3=data.T
x3 = data3.values[0]
y3 = data3.values[1]
#pyl.plot(x3,y3,"o")
#pyl.show()
#大于150认为异常值

#分布分析
pmax=data3[1].max()
pmin=data3[1].min()

cmax=data3[2].max()
cmin=data3[2].min()

#极差:最大值-最小值
prg = pmax - pmin
crg = cmax - cmin
#组距：极差/组数
pdst = prg/12
cdst = crg/12
#画price直方图
psty=npy.arange(pmin,pmax,pdst)
pyl.hist(data3[1],psty)
pyl.show()

csty=npy.arange(cmin,cmax,cdst)
pyl.hist(data3[2],csty)
pyl.show()
