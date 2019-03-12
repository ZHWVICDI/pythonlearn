#文件
#此与ppt相互补充，重复的内容不再赘述

#11.1打开文件
#语法：open(name[,mode,[buffering]]),返回值：一个文件对象
f=open(r'C:\text\somefile.txt')

    #11.1.1 文件模式mode参数的含义
        pass
    #11.1.2 缓冲 buffering参数
        #：表示使用内存来替代硬盘，是程序更快，只有使用flush或close时才更新硬盘上的数据
        #0：无缓存。1：有缓存。>1：指定缓存区大小。-1:默认缓存区大小

#11.2 基本文件方法
#文件对象的方法
    #11.2.1 读和写 read write
    f=open('somefile.txt','w')
    f.write('Hello,')
    #提供的string会追加到文件中已存在部分的后面
    f.write('world!')
    f.close()
    #指定读入多少字符
    f.read(4)#读入4个字符
    #默认读取全部
    f.read()
    #补充：seek和tell方法
    #seek(offset[,whence])方法：功能：将当前位置（进行读和写的位置）移动到offset指定的位置。参数：offset,指定位置。whence,1（相对当前位置的移动,2(相对与文件结尾的移动)
    with open(r'D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\somefile.txt','w') as f:
        f.write('0123456789')
        f.seek(5)
        f.write('Hello,world!')
    with open(r'D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\somefile.txt','r') as f:
        f.read()
    #tell()方法：返回当前文件的位置
    with open(r'D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\somefile.txt','r') as f:
        f.read(3)
        f.read(2)
        f.tell()

    #11.2.2 管道输出 pass

    #11.2.3 读写行 readline readlines writelines
    #readline()方法:功能：读取单独的一行（从当前位置到下一个换行符的出现包括换行符）。参数：默认单独一行，使用非负整数，表示读取字符的最大值。返回值：字符串
    #readlines()方法：功能：读取一个文件所有行返回一个列表。
    #writelines([str])方法：功能：将字符串列表写入文件，但注意，需要自己添加新行。参数：字符串列表

    #11.2.4 关闭文件
    #请使用with语句

    #11.2.5 使用这些基本方法
    #read(n)
with open(r"D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\testfile.txt") as f:
    f.read(7)
    f.read(4)
    #read()
with open(r"D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\testfile.txt") as f:
    f.read()
    #readline
with open(r"D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\testfile.txt") as f:
    for i in range(3):
        print(str(i)+':'+f.readline())
    #readlines:
import pprint;pprint.pprint(open(r"D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\testfile.txt"))
    #write():
with open(r"D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\testfile2.txt",'w') as f:
    f.write('this\nis no\nhaiku')
    #writelines():
with open(r"D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\testfile2.txt",'r') as f:
    lines=f.readlines()
    lines[1]="isn't a\n"
with open(r"D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\testfile2.txt",'w') as f:
    f.writelines(lines)

#11.3 对文件内容进行迭代
    #11.3.1 按字节处理
with open(r"D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\testfile2.txt",'r') as f:
    char=f.read(1)
    while(char):
        process(char)
        char=f.read(1)
    #下面一种避免了重复的代码
with open(r"D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\testfile2.txt",'r') as f:
    while True:
        char=f.read(1)
        if not char:break
        process(char)
    #11.3.2 按行操作
with open(r"D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\testfile2.txt",'r') as f:
    while True:
        line=f.readline()
        if not line:break
        process(line)
        
    #11.3.3 读取所有内容
    #如果文件不是很大，可以使用不带参数的read方法或者readlines方法。
    #read()
with open(r"D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\testfile2.txt",'r') as f:
    for char in f.read():
        process(char)
    #readlines()
with open(r"D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\testfile2.txt",'r') as f:
    for line in f.readlines():
        process(line)

    #11.3.4 使用fileinput实现懒惰行迭代
    #当文件非常大的时候，readlines会占用很多内存.
    #此时解决方法为：使用fileinput或者文件迭代器
    import fileinput:
        for line in fileinput.input(filename):
            process(line)

    #11.3.5 文件迭代器
    #在python新版本中文件对象是可迭代的，可以使用for循环,默认迭代行。
    with open(r"D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\testfile2.txt",'r') as f:
        for line in f:
            process(line)
    #文件迭代器和普通迭代器一样
    with open(r"D:\python\python_base_practice\python\programs\python模块\file_operate\fileinput_module\testfile3.txt",'w') as f:
        f.write('First line\n')
        f.write('Second line\n')
        f.write('Third line\n')
    lines=list(open('somefile.txt'));lines;first,second,third=open('somefile.txt')
    
            
        
        
