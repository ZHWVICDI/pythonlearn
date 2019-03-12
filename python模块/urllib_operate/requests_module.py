#Requests模块
#基于urllib的http库

#以get请求方式向服务器发送请求并获取服务器响应的数据集对象例子见requests_get.py
#requests所携带的参数无需序列化(函数自身已经实现序列化，直接传入字典类型即可)
requests.get(url,params)

#扩展 请求提交的6中常见方法
requests.get('http://httpbin.org/get')
requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/head')
requests.options('http://httpbin.org/options')


#以post请求带参数方式向服务器发送请求并获取服务器响应的数据集对象例子见requests_post.py

#post请求带json参数见requests_jsonparams.py

#post请求且定制headers头信息见request_headers.py

#丰富的response对象见requests_others.py
#使用requests方法后会返回一个response对象，其存储了服务器响应的内容。
#response对象常用属性：
r.status_code       #响应状态码
r.raw               #返回原始响应体，即urllib的response对象，使用r.raw.read()读取
r.content           #字节方式的响应体，会自动解码gzip和deflate压缩
r.text              #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
r.headers           #以字典对象存储服务器响应头,

#response 特殊方法:
r.json()    #内置的json解码器
r.raise_for_status#失败请求(非200响应)抛出异常
