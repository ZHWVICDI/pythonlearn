#文件写入操作

#读取一个文件：
#1.打开一个文件,取得关联后才能执行读写操作
#函数：open(文件路径，读写模式[,encoding=编码格式])

#文件路径参数：绝对路径或相对路径

#读写模式参数：r，读。w，写。a，追加。rb，二进制读。wb，二进制写。‘+’：原有功能基础上补充和完善操作。

#向文件写入一段文字
#函数：write(字符串)
#标准步骤：1.获取程序和文件关联2.写入数据。3.关闭文件对象

import os

fileDir=os.path.join(os.getcwd())
print(fileDir)

#取得关联
#input=open(fileDir+os.sep+'a.txt','w',encoding='utf8')
#向文件写入数据
#input.write("我在学习python\n")
#input.write('好好学习，天天向上。')
#关闭文件流对象
#input.close()
#print('文件写入完毕')

#with语句：能够很好处理上下文环境和异常情况，自动释放对象内存
#格式：with open(文件路径，读写模式) as 文件对象：

with open(fileDir+os.sep+'\\test\\a.txt','w',encoding='utf8') as fp:
    fp.write("我在学习poython\n")
    fp.write('好好学习')
    print('文件写入完毕')
