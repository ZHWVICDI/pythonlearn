#Pickle 模块
#实现python 对象序列化,和反序列化的重要模块

import pickle

#Pickle模块常用函数：
pickle.dump(obj,file[,protocol])        #对象序列化操作函数
pickle.load(file)                       #将file中的对象序列化读取，反序列化。
pickle.dumps(obj,[,protocol])           #将对象转换成String字符串类型,不存入文件中。
pickle.loads(string)                    #从string中读取序列化之前的obj对象，反序列化。

#pickle.dump(obj,file,[,protocol])
#功能：将obj对象进行序列化操作，并写入到file引用文件对象中。
#补充：protocol参数:0：ASCII,1:旧式二进制，2：新式二进制协议。（区别：2更高效，默认为0）
with open(r"D:\python\python_base_practice\python\programs\python模块\data_operate\testdata\dumptest.txt",'wb') as f:
    #文件读写模式为二进制读写模式。
    dict={'name':'zhw','sex':'female'}
    #这里我们写入字典对象序列化
    pickle.dump(dict,f)
    print('>>数据写入完毕。')

#pickle.load(file)
#作用：将file的数据读取并反序列化还原为之前的对象
#补充：反序列的对象同普通的对象一样
with open(r"D:\python\python_base_practice\python\programs\python模块\data_operate\testdata\dumptest.txt",'rb') as f:  
    #反序列化
    obj=pickle.load(f)
    print('>>obj->{0}',format(type(obj)))
    print(obj)

#pickle.dumps(obj[,protocol])
#作用：obj对象转换为一个字符串数据，但不存入文件中。
#补充：protocol默认为0,如果为负值或HIGHEST_PROTOCOL,则使用最高的协议
#定义一个列表对象
lstInfo=[1,2,3,4,'abc',True];data1=pickle.dumps(lstInfo);print('lstInfo序列化数据：',end=' ');print(data1)

#pickle.loads(string)
#作用：将string字符串反序列化还原为之前的对象
data2=pickle.loads(data1);print('lstInfo反序列化数据',end=' ');print(data2)
