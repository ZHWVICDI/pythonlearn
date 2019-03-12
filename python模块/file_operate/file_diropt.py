import os
#判断文件夹是否存在
if not os.path.exists('createDir'):
    #创建一个文件夹
    mkdir('createDir')

#删除一个文件
os.rmdir('createDir')
