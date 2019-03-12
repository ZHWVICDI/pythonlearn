#requests_headers.py
#实现以post请求带json方式且定制headers头信息向服务器发送请求并获取服务器响应的数据集对象
import requests
url='http://httpbin.org/post'

#设置头部user-agent信息
headers={
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
    'Host':'httpbin.org'
    }
#post请求带参数方式向服务器发送请求并获取相应的数据集对象
response=requests.post(url,headers=headers)

if response.status_code==200:
    print(response.text)
