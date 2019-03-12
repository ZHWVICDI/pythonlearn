#json模块
#用于完成对json文件的解析操作
import json

#常用函数
json.dumps(obj)            #完成obj对象的序列化编码为json格式操作，返回：一个json串对象
json.loads()            #完成对json数据的反序列化，返回一个原始对象
json.dump(obj,file)     #将序列化后的json字符串写入文件和从文件中读取字符串反序列化成对象
json.load(file)


#python和json对象转换
#序列化转换为json
dict==object
list,tuple==array
str==string
int,float==number
True==true
False==false
None==null
#反序列化转换为python类型
object==dict
array==list
string==str
number(int)==int
number(real)==float
ture==True
false==False
null==None



