#os模块--提供多个访问操作系统服务的功能。
#os模块有很多内容，其中一些和文件操作紧密相关。
#处理路径的函数--可以让我们大部分情况忽略掉os.pathsep

#os模块中一些重要的函数和变量
os.environ          #对环境变量进行映射,本质上是一个字典
    #访问PYTHONPATH环境变量
    os.environ['PYTHONPATH']
os.system(command)  #在子shell中执行操作系统命令
os.sep              #路径中的分隔符
os.pathsep          #分隔路径的分隔符。即window中的';'.UNIX中的‘：’MAC中的‘;;’
os.linesep          #行分隔符('\n','\r','\r\n')。windows:\r\n.UNIX:\n.MAC:\r
os.urandom(n)       #返回n字节的加密强随机数据
os.startfile(r'E:\软件\360Chrome\Chrome\Application\360chrome.exe') #执行外部程序;这是windows独有的函数

#补充：webbrowser模块：包括open函数，可以自动启动web浏览器访问给定的URL。
import webbrowser;webbrowser.open(r'http://www.baidu.com')
