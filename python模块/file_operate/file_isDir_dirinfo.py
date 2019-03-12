## 判断文件夹或文件

#判断当前文件路径是否为文件夹
#函数os.path.isdir(文件对象)，返回值：bool
import os
## 获取文件夹的信息

#查看当前文件夹中的文件名称（不会继续查看文件夹中的子文件夹内容）
#函数：os.listdir(),返回值：一个列表对象，若参数为空，则返回当前工程文件夹中的所有文件名称
lstDir1=os.listdir()#不带参数
print("当前工程文件夹中的文件：{0}".format(lstDir1))
#注意工程文件夹指的是python工作的那个文件夹

#获取指定文件夹中的文件名称
lstDir2=os.listdir('D:\python\python_base_practice\python\programs\python模块\\file_operate')#改为指定目录
print('指定目录中的文件名称：{0}'.format(lstDir2))

#获取文件夹的信息os.walk()函数
#os.walk(文件地址)：返回值：文件路径地址（字符串）、文件夹集合(列表)和文件夹中的文件(列表)

#常规使用：for+os.walk()组合，实现对指定文件夹的深度遍历
for root,dirs,files in os.walk("D:\python\python_base_practice\python\programs\python模块\\file_operate"):
    print('|-文件夹路径：%s'%root) #获取文件夹所有目录及子目录名称。
    print('||-路径下的文件夹：{0}'.format(dirs))#获取当前文件夹的子文件夹名称
    print('|||-文件夹中的文件：{0}'.format(files))
    pass
