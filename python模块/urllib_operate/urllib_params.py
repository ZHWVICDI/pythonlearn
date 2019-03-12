#urllib_params.py
import urllib.request,os
import pickle

def write2file(response,f):
    dirPath=os.path.join(os.getcwd(),'datatest')
    with open(os.path.join(dirPath,f),'w',encoding='utf8') as fp:
        fp.write(response.read().decode('utf-8'))
        print(">>>网页源代码写入完毕")
    

url='https://book.douban.com/subject_search'
#设置请求参数(要符合网站的定义格式)
dictParams={'search_text':'粉墨','cat':1001}
#将请求参数字典类型序列化为字节流
data=pickle.dumps(dictParams)

#发送访问请求并携带参数
response=urllib.request.urlopen(url,data=data)
#判断连接是否正常
if response.getcode()==200:
    #写入指定文件
    write2file(response,'book.douban.html')
print('>>>文件写入完毕')
