#csv_test.py
import csv,os
filePath=os.path.join(os.getcwd(),'testdata')

#将数据写入csv文件
#这里是使用writer()写入数据
columns=['姓名','年龄','电话']
#准备写入的数据
data=[('测试人员1',18,'13213213131'),
      ('测试人员2',24,'1321343213131'),
      ('测试人员3',23,'1323413213131'),]

#这里encoding参数设置为gb18030防止中文乱码，newline参数防止多一个空行
with open(filePath+os.sep+'data.csv','w',encoding='gb18030',newline='') as csvfile:
    #获取writer写入对象
    writer=csv.writer(csvfile)
    #这里写入数据标题行（单行数据）
    writer.writerow(columns)
    print('数据标题行写入完毕')
    #写入多行数据
    writer.writerows(data)
    print('数据多行写入完毕')
    
#将数据从csv文件中读取出来，并且打印
with open(filePath+os.sep+'data.csv','r',encoding='gb18030') as csvfile:
    #使用csv.reader()读取csv数据
    reader=csv.reader(csvfile)
    print('>>reader Type->{0}'.format(reader))
    #使用for循环遍历reader对象
    for line in reader:
        print(line)

#读取csv文件，获取后的数据使用dict直接转化为字典数据，键为标题字段
def getCsvData():
    with open(filePath+os.sep+'data.csv','r',encoding='gb18030') as csvfile:
        #使用csv.reader()读取csv数据
        reader=csv.DictReader(csvfile)
        print('>>reader Type->{0}'.format(reader))
        #使用for循环遍历reader对象
        return [dict(line) for line in reader]
print(getCsvData())

#将字典数据写入csv文件
#准备写入的数据：
data2=[{'字段1':-1,'字段2':-2},{'字段1':1,'字段2':2}]
#写入文件
with open(filePath+os.sep+'data3.csv','w',encoding='gb18030') as csvfile:
    #获取所有字典数据的key部分??--这里的含义是：获取第一个字典，然后遍历他，默认为键。
    keys=[k for k in data2[0]]
    #使用DictWriter()读取数据,fieldnames参数就是指定域的名字
    writer=csv.DictWriter(csvfile,fieldnames=keys)
    #调用writerheader()方法写入数据标题
    writer.writeheader()
    print('标题写入完毕')
    ##循环遍历数据
    for d in data2:
        #使用writer()函数写入
        writer.writerow(d)
    print('数据写入完毕')
    

