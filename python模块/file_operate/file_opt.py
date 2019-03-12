import os
import time
from os.path import join,getsize

def TimeStampToTime(timestamp):
    '顶一个时间戳格式化函数'
    #获取时间属性（年月日时分秒）
    timeStruct=time.localtime(timestamp)
    #格式化输出返回
    return time.strftime("%Y-%m-%d %H:%M:%S",timeStruct)


def calcFileSize(absolutePath):
    '计算文件的大小'
    print('开始计算文件大小......')
    #获取文件的大小
    size=os.path.getsize(absolutePath)
    return size

def calcDirSize(absolutePath):
    '输出文件夹的大小及操作日期数据'
    #获取文件的大小
    fileSize=os.path.getsize(absolutePath)
    #使用os.walk+for深度遍历文件夹中的文件
    size=0#用于累加子文件大小
    for root,dirs,files in os.walk(absolutePath):
        print('|-文件夹路径：%s'%root) #获取文件夹所有目录及子目录名称。
        print('||-路径下的文件夹：{0}'.format(dirs))#获取当前文件夹的子文件夹名称
        print('|||-文件夹中的文件：{0}'.format(files))#获取当前子文件夹中的文件名称
        #使用sum(数字序列)函数
        size+=sum(getsize(os.path.join(root,name)) for name in files)
    return size

def fileDetials(filePath):
    '输出文件基本信息'
    os.system('cls')#清屏操作
    #获取文件的绝对路径
    absolutePath=os.path.realpath(filePath)
    #判断文件路径的文件类型？？？？这个语句
    fileType='文件夹' if os.path.isdir(absolutePath) else '文件'
    #计算文件对象大小
    #异常处理
    try:
        #根据文件类型输出不同结果
        size=calcDirSize(absolutePath) \
              if fileType=='文件夹' \
              else calcFileSize(absolutePath)
        
    except FileNotFoundError:
        print("输入的文件或文件夹路径有误，核实后输入")
        os.exit(0)#退出系统
        
    #获取文件名称
    fileName=os.path.basename(absolutePath)
    #获取文件的所在目录
    dirPath=os.path.dirname(absolutePath)
    #输出
    print('\n-------------文件对象信息-------------')
    print("对象名称：{0}".format(fileName))
    print("所在目录：{0}".format(dirPath))
    print("文件类型：{0}".format(fileType))
    print("对象的大小：{0}字节".format(size))
    
    #获取文件的创建时间
    createTime=os.path.getctime(absolutePath)
    print("对象创建时间：{0}".format(TimeStampToTime(createTime)))
    
#获取文件的访问时间
    accessTime=os.path.getatime(absolutePath)
    print("对象访问时间：{0}".format(TimeStampToTime(accessTime)))
    #获取文件的修改时间
    modifyTime=os.path.getmtime(absolutePath)
    print("对象修改时间：{0}".format(TimeStampToTime(modifyTime)))
    
pass
