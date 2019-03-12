#二进制文件的读写操作
#实现图片文件的复制
#标准步骤：1.读取2.写入

import os

fileDir=os.path.join(os.getcwd(),'test')
print(fileDir)

content=0
#读取二进制文件
with open(fileDir+os.sep+'test.jpg','rb') as fp:
    content=fp.read()
    pass

with open(fileDir+os.sep+'test(1).jpg','wb') as fp:
    #写入数据
    fp.write(content)
    print('二进制文件写入完毕')

