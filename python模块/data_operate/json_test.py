import json,os
filePath=os.path.join(os.getcwd(),'testData')

#定义一个字典类型对象
data={'pid':'p001','pname':'测试商品名称','price':299}

#使用json.dumps()完成对象序列化转换为json字符串
strJson=json.dumps(data,ensure_ascii=False)#防止中文数据乱码

#测试输出
print('data原始数据：{0}'.format(data))
print('json转换数据：{0}'.format(strJson))
#这里的类型为字符串
print(type(strJson))

#使用json.loads完成json->对象的转换
obj=json.loads(strJson)
print('obj->{0}'.format(type(obj)))
print('pid:{0}'.format(obj['pid']))
print('pname:{0}'.format(obj['pname']))
print('price:{0}'.format(obj['price']))

#定义一个字典类型对象
data2={'pid':'p002','pname':'测试商品名称2','price':29}
with open(filePath+os.sep+'data.json','w',encoding='utf8') as fp:
    #使用json.dump()完成对象转换为json字符串并存入文件
    json.dump(data2,fp)
    print('json文件数据写入完毕.')
    pass

with open(filePath+os.sep+'data.json','r',encoding='utf8') as fp:
    #使用json.load将读取文件中的json字符串并反序列化为对象。
    data3=json.load(fp)
    print('dataType->{0}'.format(type(data3)))
    print('>>{0}'.format(data3))
    pass
