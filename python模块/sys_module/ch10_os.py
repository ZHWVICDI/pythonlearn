#sys模块

#sys模块中一些重要的函数和变量
sys.argv        #命令行参数，包括脚本名称,一个列表。脚本名为argv[0],后面为参数。
sys.exit([arg]) #退出当前程序，可选参数为给定的返回值或错误信息；一般提供默认值0表示成功。
sys.modules     #映射模块名字到载入模块的字典
sys.path        #查找模块所在目录的目录名列表
sys.platform    #平台标识符，可能是标识操作系统的名字，可能是其他平台，如java虚拟机。
sys.stdin       #标准输入流--类文件对象
sys.stdout      #标准输出流--同上
sys.stderr      #标准错误流--同上
