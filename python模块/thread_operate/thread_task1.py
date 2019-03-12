#实战任务--统筹方法
import threading,time
#创建洗杯子线程类
class WashCup(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,5):
            print('开始洗第',i,'个杯子...')
            time.sleep(3)
            print('第',i,'个杯子洗完了！')

#创建煮水子线程类
class BoilWater(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        print('开始煮水...')
        time.sleep(10)
        print('水煮好了！')

if __name__=='__main__':
    BoilWater().start()
    WashCup().start()
