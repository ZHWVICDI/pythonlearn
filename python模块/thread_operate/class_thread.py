#导入线程模块
import threading
import time
#创建退出标志位变量
exitFlag=0

#自定义一个输出函数
def outputTime(threadName,delay,counter):
    while counter:
        if exitFlag:
            threading.Thread.exit()
        time.sleep(delay)
        print('%s:%s'%(threadName,time.ctime(time.time())))
        counter-=1
    pass

#创建线程类
class MyThread(threading.Thread):
    #重写构造方法
    def __init__(self,threadID,name,counter):
        #调用父类构造方法
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    #重写run方法
    def run(self):
        print('启动->'+self.name)
        outputTime(self.name,5,self.counter)
        print('结束->'+self.name)
    pass

#脚本程序入口
if __name__=='__main__':
    print('mainThread主线程启动...')

    #创建两个线程
    thread1=MyThread(1,'Thread-1',1)
    thread2=MyThread(2,'Thread-2',1)
    #启动线程
    thread1.start()
    thread2.start()

    print('mainThread主线程结束')
