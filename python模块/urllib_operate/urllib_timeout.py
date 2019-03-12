#urllib_timeout.py
import urllib.request,os
import socket

url='https://book.douban.com'

try:
    #发送访问请求并携带参数
    response=urllib.request.urlopen(url,timeout=0.1)
    print(response.getcode())
except socket.timeout:
    print('>>>连接请求超时')
