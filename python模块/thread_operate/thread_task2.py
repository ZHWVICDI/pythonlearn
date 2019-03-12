#thread_task2.py
import threading
import time
import random

#使用共享区模拟变量
count=0
#创建条件对象
condition=threading.Condition()

#生产者线程类
class Producer(threading.Thread):
    def __init__(self,threadName):
        threading.Thread.__init__(self)
        self.threadName=threadName
    def run(self):
        global count  #引用全局共享变量count
        while True:
            #使用条件对象获取锁并锁定
            if condition.acquire():
                #判断共享变量是否达到上限
                if count>=10:
                    print('共享区已满，生产者producer线程进入阻塞状态，停止放入！')
                    condition.wait()#当前线程进入阻塞状态
                else:
                    count+=1#共享变量加1
                    msg=time.ctime()+' '+self.threadName+'生产了1件商品放入共享区，共享区总计商品个数：'+str(count)
                    print(msg)
                    condition.notify()#唤醒其他阻塞状态的线程
                condition.release()#解除锁定
                time.sleep(random.randrange(10)/5)#随机休眠N秒

#消费者线程类
class Customer(threading.Thread):
    def __init__(self,threadName):
        threading.Thread.__init__(self)
        self.threadName=threadName
    def run(self):
        global count
        while True:
            #使用条件对象获取锁并锁定
            if condition.acquire():
                #判断共享变量是否为0（已空）
                if count<1:
                    print('共享区已空，消费者customer线程进入阻塞状态，停止获取！')
                    condition.wait()
                else:
                    count-=1#共享变量自减1
                    msg=time.ctime()+' '+self.threadName+'消费了1件商品，共享区总计商品个数：'+str(count)
                    print(msg)
                    condition.notify()   #唤醒其他阻塞状态的线程
                condition.release()#解除锁定
                time.sleep(random.randrange(10)/5)#随机休眠N秒

#脚本程序入口
if __name__=='__main__':
    for i in range(2):
        p=Producer('[生产者-'+str(i+1)+']')
        p.start()
    for i in range(5):
        c=Customer('[消费者-'+str(i+1)+']')
        c.start()
                
                    
