#requests_others.py
import requests
#淘宝IP地址库API
URL='http://ip.taobao.com/service/getIpInfo.php'

try:
    r=requests.get(URL,params={'ip':'8.8.8.8'},timeout=1)
    r.raise_for_status()#如果响应码不是200，就主动抛出异常
except requests.RequestException as e:
    print(e)
else:
    result=r.json()#Requests中内置的json解码器
    print(type(result),result,sep='\n')
