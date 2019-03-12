#urllib_headers.py
from urllib import request

url='http://httpbin.org/post'
#设置请求头部user-agent信息
headers={
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
    'Host':'httpbin.org'
    }

#创建request对象并设置头部信息
req=request.Request(url=url,headers=headers,method='Post')
#访问网页并返回信息数据
response=request.urlopen(req)
print(response.getcode())
