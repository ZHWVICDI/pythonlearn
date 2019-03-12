#random模块
#包括返回随机数的函数，可以模拟或者用于任何产生随机输出的程序
#补充：产生的随机数都是。需要真的随机性的话，应该使用os模块的urandom函数。random模块中的SystemRandom类也是基于同种功能，可让数据接近真正的随机性。
import random

#random模块中的重要函数

random.random()             #返回0<=n<1之间的随机实数n,其中0<n<=1
random.getrandbits(n)       #以长整数形式返回n个随机位
random.uniform(a,b)         #返回随机实数n，其中a<=n<b，例如0-360可以表示随机的角度值
random.randrange([start],stop,[step])   #返回range（start,stop,step）中的随机数
random.choice(seq)          #从序列seq中返回随机元素
random.shuffle(seq[,random])    #原地制定序列seq,也就是随机对序列移位
random.sample(seq,n)        #从序列seq中随机选择n个独立的元素(即元素互不相同)

#实例1 产生指定日期之间的随机日期
from random import *;from time  import *
#产生两个时间戳
date1=(2018,1,1,0,0,0,-1,-1,-1);time1=mktime(date1);date2=(2019,1,1,0,0,0,-1,-1,-1);time2=mktime(date2)
#在这个范围内均一产生随机数
random_time=uniform(time1,time2)
#转化时间戳为日期元组，再转换为字符串
print(asctime(localtime(random_time)))

#实例2 骰子
from random import randrange
#骰子数
numstr=input('How many dice?');num=int(numstr)
#每个骰子数有多少个面
sidestr=input('How many sides per die?');sides=int(sidestr);sum=0
for i in range(num):
    sum+=randrange(sides)+1;
    sum=0
print('The result is',sum)

#实例3 见sendcards.py

