#数字和表达式

#数字分int，float，complex类型

#整除  /  除余  %   min  **

#长整数型  int 十六进制 0x 八进制 0

#获取用户输入
x=input("info:")
print(x)

#函数

#模块导入 2种方式 推荐前一种
import math
print(math.floor(32.6))

from math import floor
print(floor(32.6))


#cmath和复数 cmath复数模块
import camth
cmath.sqrt(-1)

#1.10.1 保存运行python文件
见麒麟给的ppt

#1.11 字符串
#1.11.1单引号字符串 与双引号字符串无区别
#1.11.2拼接字符串 huo +号连接
>>> "Hello,world!"
'Hello,world!'
>>> "h"'m'
'hm'
>>> 'h' 'm'
'hm'
>>> x='j'
>>> y='k'
>>> xy
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    xy
NameError: name 'xy' is not defined
>>> x y
SyntaxError: invalid syntax
>>> 

#1.11.3字符串表示，str和repr
#1.11.4 长字符串 原始字符串 和Unicode  ''' '''或"""　""" python3中都是Unicode字符串
print('''this is a very long string.
        It continues here.
        And''')
#该转义符被忽略
print("Hello,\
world!.")

#原始字符串对反斜线不作为特殊字符,结尾不能输入反斜线。使用路径时很好用
print（r'C;\nowhere'）







