#更加抽象 -- 自定义对象
#面向对象 多态、封装、方法、特性、超类、继承
#补充：类的方法：一共四种，实例方法，类方法，静态方法，普通方法。四种方法的区别详细见ppt。
#补充：一个标准类被创建时需要遵循的四必须标准规范：1.必须定义__init__构造方法2.必须定义__str__3.类的属性必须为私有4.类必须设置公有的属性访问函数.

#7.1 对象的魔力
#面向对象的优点：多态：不同类的对象使用相同操作。封装：对外部隐藏工作细节。继承：普通类为基础建立专门的类对象。
    #7.1.1 多态 --详细的请看java的笔记和浏览器，什么时候整理一下。
    #iisinstance : 类/类型检查
    isinstance(object,tuple)#检查object是否为元组
        #多态和方法
        #方法：绑定到对象特性上的函数 pass
        # 多态的多种形式 pass
    

    #7.1.2 封装 pass
    #补充：访问修饰符：公有权限：识符开头无下划线；私有权限：标识符开头双下划线。保护权限：标识符开头单下划线。
    #公有权限：类内外部均可访问。保护权限：类本身及子类。死有权限：只有类内部可访问。    

    #7.1.3 继承 pass

#7.2 类和类型
    #7.2.2 自定义类
    #简单类实例
    __metaclass__=type#确定使用新式类

    class Person:

        def setName(self,name):
            self.name=name

        def getName(self):
            return self.name

        def greet(self):
            print("Hello,world!I'm %s."%self.name)
    #self:对于对象自身的引用,用于让成员方法访问对象的特性。
    foo=Person();bar=Person();foo.setName('Luke');bar.setName("Anakin");foo.greet();bar.greet()
    #特性：指的是类的成员属性。python的类没有权限保护。   
    #在外部访问特性
    foo.name;bar.name='Yoda';bar.greet();

    #7.2.3 特性、函数、和方法、self
    #方法和函数的区别:self参数.下面谈论的就是self参数。
    #不用self的情况；
    class Class:
        def method(self):
            print('I have a self!')
    def function():
        print("I don't...")
    instance=Class();instance.method()
    #这里的外部函数等同于绑定方法method(),这里没有self.
    instance.method=function;instance.method()
;   #注意:self参数并不取决于调用方法的方式，目前使用的实例调用方法，可以随意使用引用于同一个方法的其他变量。
    class Bird:
        song='Squaawk!'
        def sing(self):
            print(self.song)
    #变量birdsong引用绑定方法bird.sing(),这仍然是对self参数的访问(birdsong仍然绑定在类的相同实例上)
    bird=Bird();bird.sing();birdsong=bird.sing;birdsong();

    #再论私有化
    
#默认情况下，程序可以从外部访问一个对象的特性.
    #对于权限的控制，见仁见智。
    
#Python不直接支持私有方式，靠程序员自己把握在外部修改的时机。但也可小技巧达到私有特性的效果。
    #小技巧：在名字前加上双下划线，让方法或特性变为私有
    class Secretive:
        #__inaccessible从外界无法访问
        def __inaccessible(self):
            print("can't see me..")
        #在类内部还能访问
        def accessible(self):
            print('the secret message is:')
            self.__inaccessible()
    s=Secretive();
    #从外部无法访问
    s.__inaccessible();
    s.accessible();
    #原理：在类的内部定义中，所有以双下划线开始的名字都被‘翻译’为前面加上单下划线和类名的形式。
    Secretive._Secretive__inaccessible
    #访问这些私有方法。
    s._Secretive__inaccessible()
    #小技巧2:不需要使用这种方法但又想其他对象不要访问内部数据，可以使用单下划线。
    #前面有下划线的名字都不会被带星号的imports语句导入（from module import *）

    #7.2.4 类的命名空间 
    #类命名空间可以被类内的所有成员访问。
    
class MembersCounter:
        #不相当于类变量。就是特性。？？？？？
        members=0
        def init(self):
            MembersCounter.members+=1
    m1=MembersCounter();m1.init();MembersCounter.members;m2=MembersCounter();m2.init();MembersCounter.members;m1.members;m2.members;
    #重绑定members特性,这里屏蔽了类范围内的变量。
    m1.members='Two';m1.members;m2.members
    

    #7.2.5 指定超类
    #将其他类名写在class语句后的圆括号内可以指定超类
    class Filter:
        def init(self):
            self.blocked=[]
        def filter(self,sequence):
            return [x for x in sequence if x not in self.blocked]
    class SPAMFilter(Filter):#指定超类为Filter
        def init(self):#这里重写了超类中的init方法
            self.blocked=['SPAM']
    f=Filter();f.init();f.filter([1,2,3])

    #子类过滤序列中的“SPAM”
    s=SPAMFilter();s.init();s.filter(['SPAM','SPAM','eggs'])
    
    #7.2.6 调查继承
    #使用内建的issubclass函数：作用：查看一个类是否是另一个类的子类。
    issubclass(SPAMFilter,Filter);issubclass(Filter,SPAMFilter)
    #要知道已知类的基类（们），可以使用特殊特性__bases__
    SPAMFilter.__bases__;Filter.__bases__
    #isinstance函数 作用：检查一个对象是否是一个类的实例。
    s=SPAMFilter();isinstance(s,SPAMFilter);isinstance(s,Filter)#这里都为True,因为继承关系。
    #要知道一个对象属于哪个类，可以使用__class__特性
    s.__class__
    #注意：使用__metaclass__=type或从object继承的方式定义类，可使用type(s)查看实例的类。

    #7.2.7 多个超类 即python是支持多重继承的
    class Calculator:
        def calculate(self,expression):
            self.value=eval(expression)
    class Talker:
        def talk(self):
            print('Hi,my value is ',self.value)
    class TalkingCalculator(Calculator,Talker):
        pass
    tc=TalkingCalculator();tc.calculate('1+2*3');tc.talk()
    #注意:超类的顺序：先继承的方法会重写后继承的类的方法.

    #7.2.8 接口和内省
    #python中，只要关心其接口即可--即公开的方法和特性 。不用显式指定对象必须包含那些方法才能作为参数。不能实现的话，程序会失败。
    #也就是我们只要让对象符合当前接口（实现了当前方法）。
    #我们可以检查所需的方法是否已经存在。hasattr函数，参数：对象名，'方法名'，返回值：bool
    hasattr(tc,'talk')；hasattr(tc,'fsdf')
    #检查talk特性方法是否可以调用
    callable(getattr(tc,'talk',None));callable(getattr(tc,'fnord',None));
    #注意 ：setattr函数 ，用来设置对象特性
    setattr(tc,'name','Mr.Gumby');tc.name
    #查看对象内所有存储的值，使用__dict__特性。
    tc.__dict__
    #inspect模块  详细查看对象由什么组成。
    
#7.3 面向对象设计的思考
值得一看。


#可以梳理一下面向对象程序设计的一些思想和所学语言对于这些思想的实现方式。



    
    
    

      
