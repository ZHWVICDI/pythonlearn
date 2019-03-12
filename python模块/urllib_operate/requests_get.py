#requests_get.py
import requests

url='http://www.douban.com/subject_search'

#使用get函数发送请求
response=requests.get(url,params={'search_text':'粉墨','cat':1001})
#输出服务器返回数据
print('服务器返回状态码:{0}'.format(response.status_code))

if response.status_code==200:
    #response对象的text属性：获取服务器反馈的资源数据
    print(response.text)
    pass
