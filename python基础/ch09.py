#魔法方法、属性、迭代器
#重要的特殊方法（__init方法和处理对象访问的方法）


#9.1 pass 在python3.0中没有“旧式”类，不需要显式的设定元类，或子类化object类。所有的类都隐式的成为object的子类。

#9.2 构造方法 
#当对象被创建后，会立即调用构造方法。
#构造方法的作用两个：1.为对象创建内存空间。2.实例对象那个的实例变量参数初始化.

#创建构造方法：__init__
class FooBar:
    def __init__(self):
        self.somevar=42
    def __init__(self,value=42):
        self.somevar=value
    def __str__(self):
        return '自定义该类对象输出内容'
f=FooBar();f.somevar;h=FooBar("This is a constructor argument!");h.somevar
#析构方法：在对象被垃圾回收前调用，发生调用时间不可知，因为不知什么时候被回收。所以尽量避免使用。
#实例对象输出 __str__:当我们输出实例对象时，默认输出的是当前实例对象的十六进制内存地址
#我们可以重写__str__方法。类似java中的tostring方法。。。见上面的类。
f=FooBar();print(f);f#前者可以打印，后者仍然是十六进制内村地址。因为python__str__是给用户使用的，而还有一个详情见浏览器。


    #9.2.1 重写一般方法和特殊构造方法
    #python支持多重继承，子类从超类那儿继承了行为方式。如果一个方法在子类实例中被调用，但在子类中没有找到，会从其超类中寻找。
    class A:
        def hello(self):
            print("A's method")
    class B(A):
        pass
    a=A();b=B();a.hello();b.hello()
    #子类增加功能:1.增加自己的方法.2.重写超类的方法（分重写一般方法和特殊方法）。
    #重写和重载：都是多态的实现方式，具体自己查看。
    #重写构造方法：子类要重写构造方法时，需要调用超类的构造方法，否则对象不会正确地初始化。而我们不重写构造方法，子类会继承父类的构造方法。所以重写构造方法时，请调用super()函数，保证基本的初始化。
    #错误实例
    class Bird:
        def __init__(self):
            self.hungry=True
        def eat(self):
            if self.hungry:
                print('Aaaah..')
                self.hungry=False
            else:
                print('No,thanks!')
    class SongBird(Bird):
        def __init__(self):
            self.sound='Squawk!'
        def sing(self):
            print(self.sound)
    b=Bird();b.eat();b.eat()
    #因为在SongBird类没有调用Bird类的构造方法。eat()方法会出现问题。
    sb=SongBird();sb.sing();sb.eat()
    
    #9.2.2 pass 调用未绑定的超类的构造方法，以及不用了。

    #9.2.3 使用super函数:保证基本初始化
    #上例的更新版
    class Bird:
        def __init__(self):
            self.hungry=True
        def eat(self):
            if self.hungry:
                print('Aaaah..')
                self.hungry=False
            else:
                print('No,thanks!')
    class SongBird(Bird):
        def __init__(self):
            #此处调用了super函数
            super(SongBird,self).__init__()
            self.sound='Squawk!'
        def sing(self):
            print(self.sound)
    #这里运行正常，因为子类得到基本初始化，hungry特性得到初始化。
    sb=SongBird();sb.sing();sb.eat();sb.eat()

#9.3 成员访问
#注意：规则：某种形式的行为的规则。类似于接口。python的多态性基于对象的行为。其他语言可能要求继承某个类，或者实现某接口。而python只需要简单的要求遵守几个给定规则即可。举例来说；你要成为一个序列，只需要遵循序列的规则。
    
    #9.3.1 序列和映射的基本行为（规则）
    #可变对象使用4个魔法方法，不可变对象使用2个
    #需要实现的魔法方法如下：
    #__len__(self):返回集合中所含项目数量：返回0表示空
    #__getitem__(self,key):放回所给键对应的值。对序列，提供索引(参数的意思)。对映射，提供键。
    #__setitem__(self,key,value):存储key-value.随后可用__getitem__方法获取.用于可修改对象。
    #__delitem__(self,key):对对象使用del语句时被调用，必须同时删除和元素相关的键，用于可修改对象。
    #对方法的附加要求：
    #对一个序列，如果键是负整数，要从末尾开始计数。
    #当键为不合适的类型时，要引发一个TypeError异常。
    #序列索引超出范围，要引发IndexError异常。
    #实践：创造一个无穷序列,此序列为一个算术序列。
    def checkIndex(key):
        """
    所给的键是否是可接受的索引

    这里假设键应该为一个非负的整数。如果不是一个整数，引发TypeError;如果为负数，引发IndexError.因为我们假设为一个无穷序列，所以不判断越界。
    """
        if not isinstance(key,int):raise TypeError
        if key<0:raise IndexError
    class  ArithmeticSequence:
        def __init__(self,start=0,step=1):
            """初始化算术序列

                初始值---序列中第一个值
                步长---
                改变---用户修改的值的字典"""
            self.start=start
            self.step=step
            self.changed={}
        #实现了该方法，当我们访问该对象时，就可以格式：对象名[key]的访问
        def __getitem__(self,key):
            checkIndex(key)
            try:return self.changed[key]
            except KeyError:
                return self.start+key*self.step
        #实现了该方法，当我们要添加值的时候，可以格式:对象名[key]=value的形式来设置。
        def __setitem__(self,key,value):
            checkIndex(key)
            self.changed[key]=value
    s=ArithmeticSequence(1,2);s[4]; s[4]=2;
    #删除元素非法，因为我们没有实现__del__方法
    del s[4]
    #异常数据访问
    s["four"];s[-42]
    

    #9.3.2 子类化列表，字典和字符串
    
#像上述这样为了实现想列表或是字典的行为是繁重的工作，且很难做好。
    #如果只是想要在一个操作中自定义行为，可以使用继承，子类化内建类型。
    #例子：实现一个和内建列表相似的序列，我们选择子类化list
    #带访问计数的列表
    class CounterList(list):
        def __init__(self,*args):
            super(CounterList,self).__init__(*args)
            self.counter=0
        def __getitem__(self,index):
            self.counter+=1
            return super(CounterList,self).__getitem__(index)
    
    #使用;该类严重依赖其超类list的行为。
    c1=CounterList(range(10));c1;c1.reverse();del c1[3:6];c1.counter;c1[4]+c1[2];c1.counter

#9.4 更多的特殊方法。可以参考《Python参考手册》3.4节 已下载。

#9.5 属性 通过访问器定义的特性
#访问器：即getXxx（）和setXxx()方法，java中也是.
#封装状态变量
class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def setSize(self,size):
        self.width,self.height=size
    def getSize(self):
        return self.width,self.height
#这里getSize和setSize是一个名为size的假想特性的访问器方法。但如果我们需要size成为一个真正的特性，即我们需要直接r.size的方式来访问怎么做？
#当然我们可以写很多访问器方法，就像这里一样，可以使用r.getSize（）的方式来访问，但python提供了更好的方式，python可以隐藏访问器方法，让所有特性看起来一样。
r=Rectangle();r.width=0;r.height=5;r.getSize();r.setSize((150,100));r.width

    #9.5.1 property函数 使得上述假想特性size能够像普通特性一样被访问。
    class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def setSize(self,size):
        self.width,self.height=size
    def getSize(self):
        return self.width,self.height
    size=property(getSize,setSize)
    #我们可以r.size的方式访问size属性，以r.size=150,100的方式设置size的值。
    
#注意，但是这里size特性仍然取决于getSize()和setSize()的计算。
    r=Rectangle();r.width=10;r.height=5;r.size;r.size=150,100;r.width;
    #property ：参数：没有参数时，产生的属性不可读写。一个参数,属性可读的，2个参数，属性可读写，第三个参数(可选)，删除特性的方法。第4个参数，一个文档字符串。fget、fset、fdel、doc、
    #w理论上讲：应该使用property函数，而非访问器方法。
    

    #9.5.2 静态方法和类成员方法
    #静态方法和类成员方法在创建时分别被装入Staticmethod类型和Classmethod类型的对象。
    #静态方法定义：无self参数，且能被类本身直接调用；
    #类成员方法：定义时需要cls的参数，可以直接用类的具体对象调用。但cls参数自动绑定到类。
    class MyClass:
        def smeth():
            print("This is a static method")
        smeth=staticmethod(smeth)

        def cmeth(cls):
            print("This is a class method of",cls)
        cmeth=classmethod(cmeth)
    #使用装饰器语法的改进版本
    class MyClass:
        @staticmethod
        def smeth():
            print("This is a static method")
        
        @classmethod
        def cmeth(cls):
            print("This is a class method of",cls)
    MyClass.smeth();MyClass.cmeth()

    #9.5.3 __getattr__、__setattr__和其它朋友 pass如果要拦截对象的所有特性访问时，我们再回顾吧。

#补充：类的方法：一共四种，实例方法，类方法，静态方法，普通方法。四种方法的区别详细见ppt。
#补充：一个标准类被创建时需要遵循的四必须标准规范：1.必须定义__init__构造方法2.必须定义__str__3.类的属性必须为私有4.类必须设置公有的属性访问函数.
    

#9.6 迭代器    书上这里带我们了解了迭代器的规则
#__iter__：特殊方法，也是迭代器规则的基础,返回一个迭代器(总是返回自己，见下面)
#迭代器：即具有__next__方法的对象，也就是可以在for x in xs 的格式中循环的对象。
#__next__：特殊方法，实现该方法的对象为迭代器，调用该方法时，迭代器返回下一个值。
    
    #9.6.1 迭代器规则  创建迭代器对象。
    #迭代：就是循环
    #实现了__iter__方法的对象是可迭代的，实现了__next__方法的对象则是迭代器。
    #迭代器实现费波拉契数列：
    class Fibs:
        def __init__(self):
            self.a=0
            self.b=1
        #增加了__next__方法，那么该对象就是一个迭代器,返回下一个值。
        def __next__(self):
            self.a,self.b=self.b,self.a+self.b
            return self.a
        #增加了__iter__方法，那么该对象就是可迭代的，放回一个迭代器对象。该方法返回了自己
        def __iter__(self):
            return self
    #使用该类
    fibs=Fibs();
    for f in fibs:
        if f>100:
            print(f)
            break
    #提示：从可迭代对象中获取迭代器。书上的next方法以及不用，而是用next函数来取得下一个值。
    it=iter([1,2,3]);it.next();it.next()#错的
    next(it);next(it)
    
    #9.6.2 迭代器转化为序列
    #一个迭代器对象
    class TestIterator:
        def __init__(self):
            self.value=0
        def __next__(self):
            self.value+=1
            if self.value>10:raise StopIteration
            return self.value
        def __iter__(self):
            return self
    #利用list构造方法转换迭代器为列表
    ti=TestIterator();list(ti)

#9.7 生成器 本质也是一种迭代器，让其可以通过for in 语法来访问.不使用都是可以的。
#生成器 ：一种用普通函数语法定义的迭代器，任何包含yield语句的函数。为了更优雅的代码。
#生成器工作：不会直接返回值，而是每次会产生多个值。每次产生一个值（使用yield语句的地方），函数会冻结住--即函数停在该点等待被激活。函数被激活后从停止的那个点开始执行。

    #9.7.1 创建生成器
    #遍历列表的列表的例子
    #列表的列表
    nested=[[1,2],[3,4],[5,6]]
    #使用生成器遍历该列表
    def flatten(nested):
        for sublist in nested:
            for element in sublist:
                yield element
    #通过生成器来迭代使用
    for num in flatten(nested):
        print(num)

    #补充：循环生成器，也即生成器推导式（生成器表达式）：和列表推导式类似，不过返回的是生成器(并且不会立即进行循环)。
    #也就是说可以用next函数一个个获取值
    g=((i+2)**2 for i in range(2,27));next(g)
    #小技巧：生成器推导式可以在当前圆括号内直接使用,如在函数调用中。
    sum(i**2 for i in range(10))

    #9.7.2 递归生成器 
        
