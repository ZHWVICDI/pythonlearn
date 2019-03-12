#多线程python
#每个独立的线程都有一个程序运行的入口和程序的出口
#一个python脚本程序运行，python虚拟机就启动了一个进程，同时启动一个主线程mainThread
#我们可以在python程序中创建多个子线程

#python实现多线程的方式：
#1.函数方式（涉及_thread模式）
#2.用类来包装线程对象（涉及threading模块···）
#区别：_thread提供了低级别的，原始的线程以及一个简单的锁。

#函数实现多线程
#python提供的_thread模块
#调用start_new_thread()函数来创建并启动新线程
#语法：
import _thread
_thread.start_new_thread(function,args[,kwargs])
#参数：
#function：线程函数
#args:传递给线程函数的参数，必须为tuple类型
#kwargs:可选参数
#例子见func_thread.py

#线程的结束一般依靠线程函数的自然结束，也可以在线程函数中调用thread.exit()，抛出SystemExit exception，达到退出线程的作用。

#模块实现多线程
#threading模块提供的方法：
import threading
threading.currentThread()       #返回当前的线程变量
threading.enumerate()           #返回一个包含正在运行的线程的list.正在运行的线程指线程启动后和结束前的线程
threading.activeCount()         #返回正在运行的线程的数量，与len(threading.enumerate())有相同的结果

#线程模块的threadlind.Thread类：处理线程，提供的方法有：
run()           #用于表示线程活动的方法
start()         #启动线程活动
join([time])    #等待至线程终止。阻塞调用线程直至线程的join()方法被调用终止-正常退出或抛出未处理的异常或者可选的超时发生
isAlive()       #返回线程是否活动
getName()       #返回线程名
setName()       #设置线程名

#使用模块实现多线程
#python的threading模块
#语法：线程类必须重写__init__()和run方法
#1.导入线程模块
import threading
#2.创建线程类
class 线程类名(threading.Thread):
    #重写__init__()类构造方法
    def __init__(self,参数1,...,参数N):
        #调用父类构造方法
        threading.thread.__init__(self):
        .....
    #重写run()方法，线程启动后调用的方法
    def run(self):
        pass

#线程类创建并启动的语法
#创建线程对象
线程对象=线程类名称()
#启动线程，自动调用线程类中的run方法
线程对象.start()


#线程同步
#线程的工作状态：新建、就绪、运行、死亡、阻塞

#线程同步运行：之前的例子多个线程都是随机模式执行，有哪个线程占用cpu无法控制。这是我们需要线程同步技术来强行要求某个线程执行完毕之后执行另一个线程

#线程同步技术：1.锁同步2.条件变量同步
#***********
#锁：将一个线程的run()方法进行锁定，在全部执行完毕后解除锁定。使得其他线程在执行时需要等待执行中的线程解除锁定后继续执行。
#注意：锁定和解锁必须成对出现。

#创建线程锁的语法
线程锁对象=threading.Lock()

#锁定及解锁的语法：
线程锁对象.acquire()#锁定
线程锁对象.release()#解除锁定


#如何使用线程锁：将run()方法中的执行语句使用锁定和解除锁定两条语句保围起来就行
#实例见sychoronized_thread.py

#***********
#条件变量同步：
#Python提供Condition对象提供了对复杂线程同步问题的支持
#Condition:除了提供类似Lock的acquire和release方法,还提供wait和notify方法
#可认为Condition对象维护了一个锁(Lock/Rlock)和一个waiting池
#线程通过acquire获取Condition对象，调用wait方法时，线程释放锁进入blocked状态，同时waiting池中记录该线程。调用notify方法，Condition对象从waiting池中挑选一个线程，尝试获取锁。
#Condition对象的构造函数接受一个Lock/Rlock对象作为参数，若未指定，则Condition对象会自行创建一个Rlock
#Condition.notifyAll方法:作用：通知waiting池中所有线程尝试得到锁，防止有线程永远处于沉默状态。因为waiting状态的线程只能通过notify方法唤醒。

#条件变量：类似于信号量机制，条件变量就是定义的信号量，而wait方法就是p操作,notify方法就是v操作。


#生产者消费者模式例子见thread_task2.py

