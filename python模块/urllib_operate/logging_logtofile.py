#logging_logtofile.py
import logging
import os
import time

##首先创建并设置日志logger对象

#创建loggger对象并设置信息源对象名称
logger=logging.getLogger(__name__)
#设置日志的输出的输出级别这里是替代logging.basicConfig函数
logger.setLevel(logging.INFO)
#设置日志的输出格式
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

##其次，创建并设置FileHandler对象

dirPath=os.path.join(os.getcwd(),'datatest/log')
if not os.path.exists(dirPath):
    os.mkdir(dirPath)
logFileName=time.strftime('%Y%m%d%H%M%S',time.localtime())+'.log'
logPath=dirPath+os.sep+logFileName
#创建FileHandler对象
fileHandler=logging.FileHandler(logPath)
#设置Filehandler对象的写入信息级别
fileHandler.setLevel(logging.INFO)
#设置FilerHandler对象的信息格式
fileHandler.setFormatter(formatter)

##最后，logger对象添加FileHandler对象，并测试输出
logger.addHandler(fileHandler)

##补充，想将日志同时输出到控制台
#创建一个StreamHandler对象
consoleHandler=logging.StreamHandler()
#设置控制台输出信息的级别
consoleHandler.setLevel(logging.INFO)
#设置consoleHandler对象的信息格式
consoleHandler.setFormatter(formatter)
#最后为logger对象添加handler对象替换默认的handler对象
logger.addHandler(consoleHandler)


#测试输出不同级别的日志信息
logger.fatal('系统崩溃或发生致命性错误导致程序中断时需要输出的信息')
logger.critical('系统资源耗尽时需要输出的信息(一般很少用到)')
logger.error('系统报错异常时需要输出的信息')
logger.warning('系统运行警告时需要输出的信息')
logger.info('一般信息数据')
logger.debug('测试调试时需要输出的信息数据')
