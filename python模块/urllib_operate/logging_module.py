#logging模块
#内置模块，用于输出运行日志，可以设置输出日志的等级，保存路径，日志文件回滚等。
#与print区别
#1.可通过设置不同的日志等级，输出重要信息
#2.可决定讲信息输出到什么地方，以及怎么输出

#习惯上将程序中的信息分等级，信息设置为不同的日志等级，便于后续控制输出
#日志等级：使用范围(由高到低顺序):
#FATAL:致命错误
#CRITICAL:特别糟糕的事情，如内存耗尽、磁盘空间为空等
#ERROR:发生错误时，如IO操作失败或者连接问题
#WARNING:发生很重要的事件，但是并不是错误时，如用户登录密码错误
print()
#INFO：处理请求或者状态变化等日常事务
#DEBUG:调试过程中使用DEBUG等级，如算法中每个循环的中间状态


#logging的使用
#首先使用logging.basicConfig()函数设置日志信息的输出格式
#基本语法：参数说明：level:设置输出的级别。format:设置信息格式参数。
#1.%(asctime)s：系统内时间。
#2.%(name)s:信息源名称。
#3.%(levelname)s:信息等级。
#4.%(message)s:信息内容
logging.basicConfig(level=?,format=?)
#然后设置日志信息源的名称，并返回一个logger对象
logger=logging.getLogger(__name__)
#__name__参数：系统级变量获取运行对象名称。

#实例：配置logging基本的配置，然后再控制台输出日志。例子见logging_logger.py

#日志写入到文件
#FileHandler对象可以帮助我们将输出的日志信息写入到指定的文件中。
#实现步骤：
#1.创建并设置logger对象
#2.创建并设置FileHandler对象
#3.logger对象重新添加并替换默认原有的Handler处理器
#实例见logging_loggertofile.py

#如果又想写入文件又想在控制台输出
#控制台输出，需要一个StreamHandler对象
#我们仅需要创建一个，然后添加到logger对象即可为日志logger对象增加一个输出方式。
#见logging_loggertofile.py
