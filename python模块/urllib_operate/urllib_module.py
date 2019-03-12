#urllib 模块
#python内置的http请求库
#包括子模块
#1.urllib.request请求模块
#2.urllib.error异常处理模块
#3.urllib.parse url解析模块
#4.urllib.robotparser robots.txt解析模块



#urllib.request模块
#主要作用：向互联网服务器发送请求，并获取反馈数据信息
#urlopen()函数:作用：与指定网络资源建立一个连接(主要通过url)
import urllib.request
#函数原型：
urllib.request.urlopen(url,data=None[,timeout],...)
#参数说明：url:网页地址。data：请求参数数据,timeout:请求超时时间

#例子：快速获取网页的信息数据，见urlopen.py
#response服务器响应对象的一些方法
response.geturl()   #获取请求url地址
response.getcode()  #获取返回码(200正常)
response.getinfo()  #获取网页返回信息

#urlopen参数data：用于设置请求参数，为字典类型数据。
#列子：向指定的网址发送请求并携带请求参数见urllib_params.py

#urlopen参数timeout:用于设置客户端连接请求超时时长
#如果服务器未能按时返回数据则抛出socket.timeout异常
#例子：见urllib_timeout.py ？？？？

#网站405/403报错
#405/403表示网站拒绝访问
#很多网站为防止程序爬虫爬网站，会需要携带一些headers头部信息才能访问
#最常见的是user-agent参数
#例子 见urllib_headers.py  ？？？？

#实现网络资源下载
#只要获取网络图片、音频或视频等二进制资源的地址，直接连接资源并以二进制写入文件即可
#response.read() 返回数据类型为字节
#例子见urllib_download.py

#实战任务实现多线程下载器见urllib_example.py

