#抽象----即函数

#我们应该做的是抽象程序，以便下次使用，而不是每次都去重新编写函数。

#6.3创建函数 
#内建callable函数 用来判断是否是可调用的函数。
import math;x=1;y=math.sqrt;callable(x);callable(y)
#定义函数 def：这里创建一个返回费波拉契列表的函数
def fibs(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result
#执行函数
fibs(10)

    #6.3.1 记录函数：给函数写文档，以便让该函数被后面人理解．
    #可以加注释或者编写文档字符串
    #文档字符串：一般在def语句后面以及模板或者类的开头，作为函数的一部分存储。
    def square(x):
        'Calculates the square of the number x.'
        return x*x
    #访问文档字符串，使用__doc__属性
    square.__doc__
    #内建的help函数：得到函数的信息,包括文档字符串的信息。
    help(square)

    #6.3.2 所有函数都返回了东西:当不需要返回值时，返回的是None.

#6.4 参数魔法 --函数的参数
    #6.4.1 函数形参和实参的区别

    #6.4.2 改变参数--即在函数内为参数赋予新值不会改变外部任何变量的值
    #注意：参数存储在局部作用域 
    #这里以字符串(数字和元组)这类不可变的作为参数。这里外部变量不变
    def try_to_change(n):
        n='Mr.Gumby'
    name='Mrs.Entity';try_to_change(name);name
    #这里以列表不可变的作为参数.这里外部变量改变了。
    def change(n):
        n[0]='Mr.Gumby'
    names=['Mrs.Entiry','Mrs.Thing'];change(names);names
    #通过复制列表的切片，来避免这种情况。因为列表切片总是一个副本，不会影响原列表。
    n=names[:] ;n is names;n==names;n[0]='Mr.zhw';n;names;
    #总结：就是值传递和地址传递。可变序列属于地址传递。
    #2. 如果参数不可变
    #在python中，函数只能修改参数对象本身。
    #如果真的想要改变参数，可以将值放在列表中。
    def inc(x):x[0]+=1
    foo=[10];inc(foo);foo

    #6.4.3 关键字参数和默认值
    #位置参数：参数所在位置很重要,之前的都是位置参数.
    #定义两个函数
    def hello_1(greeting,name):
        print('%s,%s!'% (greeting,name))
    def hello_2(name,greeting):
        print('%s,%s!'% (name,greeting))  
    #关键字参数 :可以明确参数的作用。--主要在函数调用时
    #调用函数时，可以提供参数名字而不用管参数的顺序了。
    hello_1(greeting='Hello',name='world');
    hello_1(name="world",greeting='Hello');
    #关键字参数另一个作用是可以在函数中给参数提供默认值。主要在函数定义时
    def hello_3(greeting='Hello',name='world'):
        print('%s,%s!'% (greeting,name))
    #当参数具有默认值，调用时就可以不用或少提供参数
    hello_3();hello_3('Greetings');hello_3('Greetings','universe')
    #位置参数和关键字参数联合使用。
    #注意：位置参数放置在前面
    def hello_4(name,greeting="Hello",punctuation='!'):
        print('%s,%s%s'%(greeting,name,punctuation))
    hello_4("Mars");hello_4('Mars','Howdy');hello_4('mars',punctuation='?')

    #6.4.4 收集参数--即可以让用户提供任意数量的参数.也即让我们的函数可以将任意的参数收集起来，也即定义函数时使用*和**
    # * ：收集其余的位置参数。
    #定义函数时,将所有值放置在同一个元组中（其余的）
    def print_params(*params):
        print(params)
    print_params('Testing');print_params(1,2,3)
    #收集参数联合普通参数
    def print_params_2(title,*params):
        print(title);
        print(params)
    print_params_2('params',1,2,3)
    # ** :收集其余的关键字参数。
    #这里就是放在字典中。
    def print_params_3(**params):
        print(params)
    print_params_3(x=1,y=2,z=3)
    #普通参数和关键字参数和收集参数联合
    def print_param_4(x,y,z=3,*pospar,**keypar):
        print(x,y,x)
        print(pospar)
        print(keypar)
    print_param_4(1,2,3,5,6,7,foo=1,bar=2)

    #6.4.5 反转过程 即我们在调用函数时使用*和**
    def add(x,y):return x+y;
    params=(1,2);add(*params)
    params={'name':'zhw','greeting':'Well'};hello_3(**params)
    #*号只有在定义函数或者调用函数这两个中一个的时候用，才有效果。
    #*号同时使用在定义函数和调用函数时,和同时不用效果一样。
    def without_stars(kwds):
        print(kwds['name'],'is',kwds['age'],'years old')
    def with_stars(**kwds):
        print(kwds['name'],'is',kwds['age'],'years old')
    args={'name':'Mr.Gumby','age':42};with_stars(**args);without_stars(args);
    #提示： 在使用(*arg1,**arg2)这样不用担心参数个数的问题。
    
#6.5 作用域
#内建函数vars 返回一个变量和其对应值的“不可见”的字典,即命名空间。
x=1;scope=vars();scope['x'];vars()
#除去全局作用域外，每个函数调用都会创建一个新的作用域。
#不严谨的在函数内部直接访问全局变量,请慎重使用全局变量。
def combine(parameter):print(parameter+external)
external='berry';combine('Shrub')
#屏蔽的问题：如果局部变量或参数的名字和想要访问的全局变量相同的话，不能直接访问，全局变量会被局部变量屏蔽。
#确实需要访问的话：可以使用globals函数获取全局变量值，返回一个字典。locals函数返回局部变量的字典。
def combine(parameter):
    print(parameter+globals()['parameter'])
    print(locals())
parameter='berry';combine('Shrub')
#重绑定全局变量--使得变量引用其他新值。#global ：将变量申明为全局变量。
x=1;
def change_global():
    global x
    x+=1
change_global();x

#新的点，闭包！！！嵌套作用域
def foo():
    def bar():
        print("Hello,zhw!")
    bar()
foo()
#嵌套的应用：需要一个函数“创建”另一个函数。
def multiplier(factor):
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor
#调用该嵌套函数：
double=multiplier(2);double(5);triple=multiplier(3);triple(3);multiplier(5)(4)
#类似multiplyByFactoe函数存储子封闭作用域的行为叫闭包
#python3.中，nonlocal被引入，让用户可以对外部作用域（非全局作用域）的变量进行赋值。

#递归  pass

#阶乘和幂 pass

#二元查找 标准库中的bisect模块可以高效实现二元查找.
 
#lambda表达式 详见浏览器
