#文件读取操作

#read函数
#标准步骤：1.获取文件关联2.读取并输出

import os

#这里是将test加入到当前目录中来
fileDir=os.path.join(os.getcwd(),'test')
print(fileDir)

with open(fileDir+os.sep+'a.txt','r',encoding='utf8') as fp:
    content=fp.read()
    print(content)
