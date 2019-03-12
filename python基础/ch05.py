#条件、循环和其他语句
#许多重复的知识点，不再赘述。


#5.1 imoprt和print的更多信息
    #5.1.2 导入函数
    import somemodule;sommodule.somefunction;
    from somemodule import somefunction,anotherfucntion,yetanotherfunction;
    #确定要导入所有功能时才使用。
    from somemodule import *;
    
#当两个模块都有open函数。
    #1.我们使用第一种方式
    import module1,module2;module1.open();module2.open()
    #2.末尾增加as字句,为其添加名字
    
#为模块添加名字
    import math as foobar
    #为函数添加别名
    from math import sqrt as foobar;foobar(4)
    from module1 import open as open1;
    from module2 import open as open2;
    
#5.2 赋值魔法
    #5.2.1 序列解包 即多个赋值操作同时进行--将多个值得序列揭开，放到变量的序列中。
    x,y,z=1,2,3;x;y;z
    #序列解包用于交换变量
    x,y=y,x;x;y
    
#序列解包用于获取函数和方法返回的元组
    scoundrel={'name':'Robin','girlfriend':'Marin'};key,value=scoundrel.popitem();key;value
    #序列解包的两边元素数量必须完全一致
    #python3 的新解包特性：使用*运算符，右边可以是可迭代对象。默认为列表哦！
    a,b,*rest=[1,2,3,4];rest;#此处书上有错

    #5.2.2 链式赋值 将同一个值赋值给多个变量。
    
x=y=somefunction();
    #等同于
    x=somefunction();y=x;
    #不一定等同于
    x=somefunction();y=somefunction();

#5.4 条件和条件语句
    #5.4.1 布尔量
    False None 0 "" () [] {} 为假
    #bool函数 与list，str，tuple ，dict用于转换他值。
    bool("")
    
    #5.4.5 关键字：if elif else 其余pass

    #5.4.6 更复杂的条件
    
    #== 及 is的区别 ：==判定两个对象的值，而is判定两者是否等同，即引用。
        x=[1,2,3];y=x;z=[1,2,3]; x==y; x==z;x is y; x is z;
    
    #5.4.7 断言 assert
    #assert ：在需要确保程序中的某个条件一定为真才能让程序正常工作的时候。
    #需要确保age变量值在0到100
    age=10;assert 0<age<100;age=111 ;assert 0<age<100;
    #可以添加字符串解释断言
    age=-1;assert 0<age<100,'The age must be realistic!'

#5.5 循环
    

    #5.5.1 while pass
    
    #5.5.2 for循环
    #for循环内建范围函数range（返回一个可迭代对象,参数：提供数字上下限）;
    for number in range(1,101):print(number)

    #5.5.3 循环遍历字典元素
    d={'x':1,'y':2,'z':3};
    for key,value in d.items():print(key,value)

    #5.5.4 迭代技巧 主要是zip和enumerate函数的使用.
        #1. 并行迭代  程序同时迭代两个序列。zip
        names=['a','b','c','d'];ages=[12,45,32,102];
        #使用索引变量i来实现
        for i in range(len(names)):print(names[i],'is',ages[i],'years old')
        #使用内建函数zip来实现，作用：压缩两个序列，并返回一个元素为元组的列表.
        zip(names,ages);
        for name,age in zip(names,ages):print(name,'is',age,'years old')
        #zip可用于应付不等长的序列，当最短的序列“用完”时停止。
        for n1,n2 in zip(range(5),range(100000)):print(n1,' ',n2)
        
        #2 编号迭代 在迭代序列中对象同时还要获取当前对象的索引
        #在字符串列表中替换所有包含'xxx'的子字符串。
        strings=['helloxxx','zhe','zhwxxx','tyq','lover']
            #(1)
            for string in strings:
	if 'xxx'in string:
		index=strings.index(string)#获得其索引
		strings[index]='[consored]'#将其替换掉
            #(2) 改进版本
            index=0
            for string in strings:
                if 'xxx' in string:
                    strings[index]='censored'
                    index+=1;
            #(3) 使用内建函数enumerate函数 作用在提供索引的地方迭代索引-值对。
            for index,string in enumerate(strings):
                if "xxx"in string:
                    strings[index]='[censored]'
            strings
            
        #3.反转和排序迭代 使用reversed和sorted函数,pass，不赘述。
            
    #5.5.5 跳出循环 break和continue pass
            #while True/break 习语
            #
while 中包含if/break语句：自然将循环分为2部分，第一部分负责初始化，第2部分在循环条件为真时使用第1部分初始化好的数据。
            #尽量避免频繁使用break语句。可读性。。呵呵
            
    #5.5.6 循环中else语句
            #break通常在找到某物时，而要当我们想要在没有跳出之前做些事情。
            #思想：使用布尔变量，再循环前设定为False，跳出后设定为True，然后使用if语句查看循环是否跳出。
            broke_out=False
            for x in seq:
                do_something(x)
                if condition(x):
                    broke_out=True
                    break
                do_something_else(x)
                if not broke_out:
                    print("not break out")
            #改写
            broke_out=False
            for x in seq:
                do_something(x)
                if condition(x):
                    broke_out=True
                    break
                else：do_something_else(x)

#5.6 列表推导式——轻量级循环
#作用：利用其他列表创建新列表
[x*x for x in range(10)]
#为列表推到式添加一个if部分；
[x*x for x in range(10) if x%3==0]
#增加更多部分在列表推导式
[(x,y) for x in range(3) for y in range(3)]
#查找名字首字母相同的男孩和女孩。##这里类似于数据库的等值连接操作。列表推倒时会检查每个可能的配对。
girls=['alice','bernice','clarice'];boys=['chris','arnold','bob'];[b+'+'+g for b in boys for g in girls if b[0]==g[0]]
#上述列子的更优方案
girls=['alice','bernice','clarice'];boys=['chris','arnold','bob'];letterGirls={};for girl in girls:letterGirls.setdefault(girl[0],[]).append(girl);print([b+'+'+g for b in boys for g in letterGirls[b[0]]])

#5.7 pass del 和exec

    #pass：代码中作为占位符使用，表示什么也不做。比如我们需要测试一个缺少语句块的代码。因为在python中空代码快是非法的。

    #del:移除一个对象的引用，及其名字本身
    x=1;del x;x
    #注意：python中不会删除值，在某个值不再使用时，python解释器会负责内存的回收。
    x=['Hello','world'];y=x;y[1]='python';x;del x;y#这里删除x不会影响y,删除的仅仅是名称。

    #exec、eval执行和求值字符串。
    #在我们需要动态创造Python代码时使用。
    
        #1. exec ： 动态创建代码字符串,执行python程序相同的方式执行字符串。无返回值
        exec("print('Hello,world!')")
        #为exec提供命名空间--一个放置变量的地方.使得代码不会干扰命名空间。
        #命名空间---放置变量的地方,也称为作用域。
        #代码受到干扰的情况
        from math import sqrt;exec('sqrt=1');sqrt(4)
        #增加字典，作为命名空间。通过 in <scope>实现.<scope>放置代码字符串命名空间的字典。
        from math import sqrt;scope={};exec('sqt=1',scope);sqrt(4)；scope['sqrt']#这里书上为python2.0的写法
        #打印scope
        len(scope);scope.keys();

        #2.eval : 计算python表达式（字符串格式）,并返回结果值。
        #eval模拟计算器
        eval(input("Enter an arithmetic expression:"))
        #同样可给eval提供命名空间.
        scope={};scope['x']=2;scope['y']=3;eval('x*y',scope)
        #exec或eval调用另一个的作用域
        scope={};exec('x=2',scope);eval('x*x',scope)

        
        

