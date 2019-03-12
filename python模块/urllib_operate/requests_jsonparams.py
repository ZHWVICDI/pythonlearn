#requests_json.py
import requests
import json
url='http://httpbin.org/post'
dictParams={'key1':'value1'}
#转换为json字符串
jsonData=json.dumps(dictParams)
#post请求带参数方式向服务器发送请求并获取相应的数据集对象
response=requests.post(url,data=jsonData)

if response.status_code==200:
    print(response.text)
