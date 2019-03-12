#获取文件创建、修改和最后访问时间

#扩展：时间戳格式化输出
#导入time模块
import time,os
#定义函数时间戳格式化函数
def TimeStampToTime(timestamp):
    #获取时间属性（年月日时分秒）
    timeStruct=time.localtime(timestamp)
    #格式化输出返回
    return time.strftime("%Y-%m-%d %H:%M:%S",timeStruct)

#查看当前文件创建时间
#函数：os.path.getctime(文件路径)，返回值：时间戳

#这里我们加入absolutePath参数
absolutePath=os.path.realpath(__file__)

createTime=os.path.getctime(absolutePath)
print("当前文件创建时间：{0}".format(TimeStampToTime(createTime)))


