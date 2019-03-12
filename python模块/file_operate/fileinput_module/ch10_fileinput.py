#fileinput 模块
#可以让人轻松的遍历文本文件的所有行。

#fileinput.input:该模块最重要的函数。返回能用于for循环遍历的对象。参数：默认，提供序列形式的一个或多个文件名，可选参数inplace：bool，True时原地处理--即在读取的源文件上修改，可能会波坏源文件内容。backup参数:备份文件名。
import fileinput

#fileinput模块中重要的函数
fileinput.input([files[,inplace[,backup]]]) #便于遍历多个输入流中的行
fileinput.filename()                        #返回当前文件的名称
fileinput.lineno()                          #返回当前（累计）的行数，即多个文件处理时，行数并不会因为更换处理的文件而重置。
fileinput.filelineno()                      #返回当前文件的行数，即每处理完一个文件，行数会重置为1.
fileinput.isfirstline()                     #检查当前行是否是文件的第一行
fileinput.isstdin()                         #检查最后一行是否来自sys.stdin
fileinput.nextfile()                        #关闭当前文件，移动到下一个文件
fileinput.close()                           #关闭序列
#例子见numberlines.py
#如何调用该脚本（2方式）
#对file1.txt到file3.txt文件的所有行进行遍历。
$python some_script.py file1.txt file2.txt file3.txt
#在UNIX中使用cat为该脚本提供参数.管道方式
$cat file.txt | python some_script.py
#运行该脚本
$python numberlines.py numberlines.py

import fileinput

for line in fileinput.input(inplace=True):
    line=line.rstrip()
    num=fileinput.lineno()
    print("%-40s #2i"%(line,num))
