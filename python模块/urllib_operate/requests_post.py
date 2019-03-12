#requests_post.py
import requests
url='http://httpbin.org/post'
#post请求带参数方式向服务器发送请求并获取相应的数据集对象
response=requests.post(url,data={'name':'alvin'})

if response.status_code==200:
    print(response.text)
