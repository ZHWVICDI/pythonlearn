#自定义一个函数
import _thread,time
def workThread(threadName,delay):
    print('[启动]>>>{0}....'.format(threadName))
    counter=0#计数器
    for i in range(delay):
        print(' |-{0}正在执行中。。。{1}'.format(threadName,i))
        counter+=1
        time.sleep(1)
    print('[停止]>>>{0}....\a'.format(threadName))
#main程序入口
if __name__=='__main__':
    print('>>>>主线程mainThread启动....')
    #将两个函数放入子线程中并启动
    _thread.start_new_thread(workThread,('Thread-1',3,))
    _thread.start_new_thread(workThread,('Thread-2',5,))
    #控制主线程执行时间
    for i in range(4):
        print('mainThread正在执行....')
        time.sleep(1)
    print('>>>>主线程mainThread停止.\a')
