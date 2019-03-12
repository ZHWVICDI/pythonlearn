#time 模块
#用于获取当前时间，操作时间和日期，从字符串读取时间以及格式化时间为字符串。
#日期表示：可以用实数（这个实数也就是时间戳，从“新纪元”的1月1日0点到现在的秒数，这个新纪元与平台有关，UNIX是1970年），或者包含9个整数的元组表示。
#日期元组如下：
(2008,1,21,12,2,56,0,21,0)#表示2008年1月21日12点2分56秒，星期一，当年的21天（无夏令时）
import time
#time模块中重要的函数：
time.asctime([tuple])           #将时间元组转换为字符串
   time.asctime()               #将当前时间格式化为字符串

time.localtime([secs])          #将秒数(时间戳)转换为日期元组，以本地时间为准
time.mktime(tuple)              #将日期元组转换为本地时间为准的秒数,也即是时间戳。

time.sleep(secs)                #休眠secs秒
time.strptime(string[,format])  #将（asctime格式化过的）字符串解析为时间元组
time.time()                     #当前时间（新纪元开始后的秒数，以UTC为准）
time.gmtime()                   #获取全球统一时间，返回值是秒数。
#localtime和mktime函数功能相反
