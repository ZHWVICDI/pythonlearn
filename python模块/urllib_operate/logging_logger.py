#logging_logger.py
import logging

#设置日志信息的输出格式,设置从INFO级别向上都输出，而不输出debug
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#创建logger对象并设置信息源对象名称
logger=logging.getLogger(__name__)

#测试输出不同级别的日志信息
logger.fatal('系统崩溃或发生致命性错误导致程序中断时需要输出的信息')
logger.critical('系统资源耗尽时需要输出的信息(一般很少用到)')
logger.error('系统报错异常时需要输出的信息')
logger.warning('系统运行警告时需要输出的信息')
logger.info('一般信息数据')
logger.debug('测试调试时需要输出的信息数据')
