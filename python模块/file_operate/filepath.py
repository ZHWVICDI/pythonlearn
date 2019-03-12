import os

#查看 当前文件的绝对路径 地址
#os.path.realpath(文件对象),返回值：指定文件对象的绝对访问路径
#__file__:Python内置的关键对象，用于获取当前文件对象的引用。

absolutePath=os.path.realpath(__file__)
print("当前文件的路径：{0}".format(absolutePath))

#查看当前文件的 所在目录绝对地址 地址
#函数：os.path.dirname(文件绝对路径),返回值：指定文件对象所在目录的绝对路径地址。

absoluteDir=os.path.dirname(absolutePath)
print("当前文件目录：{0}".format(absoluteDir))

#查看当前 文件名称
#函数：os.path.basename(文件绝对路径)，返回值：指定文件对象的名称

fileName=os.path.basename(absolutePath)
print("当前文件的名称：{0}".format(fileName))

#查看 当前工程文件夹的绝对路径 地址
#函数：os.getcwd()，返回值：返回当前工程文件夹的绝对路径地址。

projectDir=os.getcwd()
print("当前工程文件夹：{0}".format(projectDir))

#查看 当前文件大小
#函数：os.path.getsize(文件绝对路径)，返回值：指定文件对象的大小（单位为字节）

fileSize=os.path.getsize(absolutePath)
print("当前文件的大小：{0}".format(fileSize))
