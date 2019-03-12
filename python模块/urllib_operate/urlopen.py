#urlopen.py

import urllib.request
import os
#设置数据存储的文件夹
dirPath=os.path.join(os.getcwd(),'datatest')
#创建文件夹
if not os.path.exists(dirPath):
    os.mkdir(dirPath)

#设置url网址
url='http://www.douban.com'
#使用urlopen函数连接指定网址并返回响应数据对象
response=urllib.request.urlopen(url)

#文件写入操作
with open(os.path.join(dirPath,'douban.html'),'w',encoding='utf8') as fp:
    fp.write(response.read().decode('utf-8'))
    print(">>>网页源代码写入完毕")
