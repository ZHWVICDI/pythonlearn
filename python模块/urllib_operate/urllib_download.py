#urllib_download.py
import urllib.request
import os

url='https://www.python.org/static/img/python-logo.png'

#连接资源并读取资源数据
data=urllib.request.urlopen(url).read()

#写入文件
fileName=url.split('/')[-1]
#设置文件存储路径
filePath=os.path.join(os.getcwd(),'datatest')
with open(os.path.join(filePath,fileName),'wb') as fp:
    #写入二进制数据
    fp.write(data)
    print('>>>文件写入完毕')
