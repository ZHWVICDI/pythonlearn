#csv_module python的内置模块
#帮助我们快速完成对csv数据的读写操作

#csv数据：
#1.以逗号分隔值，其文件以纯文本形式存储表格数据

#2.csv文件由任意数目的记录组成，记录间以某种换行符分隔
#3.每条记录由字段组成，字段间分隔符是其他的字符或字符串，最常见是逗号或制表符
#4.csv常用于数据统计和数据分析过程中的数据存储格式

import csv

#csv的常用函数：
csv.reader(csv_file)                #读取csv数据,返回值：一个可迭代的数据类型_csv.reader,可以使用for循环遍历输出该类型对象
csv.writer(csv_file)                #写入csv数据,返回值：一个csv写入对象_csv.writer
    #_csv.writer对象的方法
    cw.writerow(数据对象)           #单行数据写入.例子中的参数为list
    cw.writerows(数据对象)          #多行数据写入.列子中的参数为list
csv.DictReader(cav_file)            #读取csv数据并转换为字典数据类型.返回值：一个csv读取对象_csv.dictreader。其获取的对象可以直接使用dict(obj)直接转化为字典数据
#为什么是字典，因为标题项做键
csv.DictWriter()                    #读取字典数据并写入csv文件：返回值：一个csv写入对象_csv.dictwriter.
    cdw.writeheader()               #用于完成标题写入
    cdw.writerow(dict)              #将字典数据写入到csv文件

