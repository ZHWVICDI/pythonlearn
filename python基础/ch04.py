#字典：python唯一内建的映射类型，通过键来引用，键可以为数字、字符串、元组。
#适用字典的情况：例如
    #表征游戏棋盘的状态，用由坐标值组成的元组来作为键。
    #存储文件修改的次数，用文件名作为键。
    #数字电话/地址簿。


#4.2 创建和使用字典
#格式：多个键和对应的值构成的对组成。键值间用：隔开，项之间用逗号隔开，整个字典用{}括起来。
#注意：字典中的键是唯一的。
phoneBook={'Alice':'2437','Beth':'9102'};
#空字典
{}

    #4.2.1 dict函数
    #通过其他映射（其他字典）或（键，值）的序列对建立字典。
    items=[('name','Gumby'),('age',42)];d=dict(items);d;d['name']
    #通过关键字参数创建字典
    d=dict(name='Gumby',age=42);d
    #不带参数，返回一个空字典
    dict()
    
#以及字典方法copy

    
#4.2.2 基本字典操作 与序列操作类似，但有所区别
    d={'Alice':'2437','Beth':'9102'};d
    #len(d)返回d中项的数量
    len(d)
    #d[k] 返回关联到键k上的值
    d['Alice']
    #d[k]=v 这里涉及到python自动添加的问题
    d[k]=v
    #del d[k]删除键为k的项
    del d['Alice'];d
    #k in d 检查d中是否含有键为k的项
    'Alice' in d;
    #区别：字典的键可以为任何的不可变类型。序列索引只能为整数。若键在字典中并不存在，为其分配一个值时，字典会自动能够建立新的项，而序列不能关联到列表范围外。
    x=[] ;x[42]='Foobar'
    x={};x[42]='Foobar';x
    #字典实例见ch04_dict.py 一个电话簿例子。
    

    #4.2.3 字典与格式化字符串。
    #格式：%(字典的键)s % 字典
    phonebook={'Alice':'2437','Beth':'9102'};"Alice's phone number is %(Alice)s." % phonebook
    #此类字符串格式化在模板系统中非常有用
    template='''<html>
        <head><title>%(title)s</title></head>
        <body>
        <h1>%(title)s</h1>
        <p>%(text)s</p>
        </body>''';
    data={'title':'My Home Page','text':'Welcome to my home page!'};
    print(template % data)

    #4.2.4 字典方法
        #1. clear 作用：清除字典中所有的项。返回值：None
        d={};d['name']='zhw';d['age']=22;d;returned_value=d.clear();d;print(returned_value)
        #情况1 此情况下，x与y指向的是同一个字典.当我们清空x时，对y一点影响也没有。
        x={};y=x;x['key']='value';y;x={};y
        #情况2 若我们想要清空原始字典中所有元素，使用clear方法。此时，y也被清空。
        x={};y=x;x['key']='value';y;x.clear();y

        #2. copy 作用：返回一个具有相同键值对的新字典(浅复制)
        x={'username':'admin','machines':['foo','bar','baz']};
        #浅复制仅仅复制了容器中元素的地址。
        y=x.copy();
        #不可变对象修改会开辟新的空间，可变对象修改不会开辟新的空间
        y['username']='mlh';
        y['machines'].remove('bar');
        y;x
        #深复制 deepcopy 使用copy模块的deepcopy函数
        #深复制 原列表的修改删除不影响复制列表的值。这里c为浅复制，d改变了可变对象，c改变。而dc不改变。
        from copy import deepcopy;d={};d['names']=['Alfred','Bertrand'];c=d.copy();dc=deepcopy(d);d['names'].append('Clive');c;dc 
        #关于赋值，浅复制，深复制，详细见浏览器。

        #3 fromkeys 作用：使用给定键建立新的字典，每个键默认对应None.参数：列表，可选默认值。
        {}.fromkeys(['name','age'])
        #直接在dict上调用方法
        dict.fromkeys(['name','age'])
        #自定义默认值
        dict.fromkeys(['name','age'],'(unkonwn)')

        #4. get 作用：访问字典项。参数：键，可选默认值。返回值：值，无的话返回None，可自定义出错返回值。
        #与直接访问的区别：直接访问在试图访问字典中不存在的项时会出异常，而get则是返回None
        d={};print(d['a'])
        d={};print(d.get('a'))
        #提供默认值
        d={};print(d.get('ad','N/A'))
        #字典方法实例见ch04_dictmethod.py

        #5 has_key 作用：检查字典中是否含有给出的键。
        d={};d.has_key('name');d['name']='zhw';d.has_key('name')
        #pass python3中无此方法

        #6. items iteritems
        #items 作用：以列表形式返回所有的字典项，列表项为（键，值）形式。
        d={'title':'python web site','url':'http://www.python.org','spam':0};d.items()
        #iteritems 作用：相同但返回一个迭代器对象而不是列表.python3中好像无此方法
        it=d.iteritems();it;list(it)

        #7. keys 和iterkeys方法 同上面

        #8. pop 作用：获得给定键的值，然后移出该键值对。参数：键.
        d={'x':1,'y':2};d.pop("x");d

        #9. popitem 作用：弹出随机的项。无参数
        #一个一个移除并处理项时
        d={'title':'python web site','url':'http://www.python.org','spam':0};d.popitem();d

        #10. setdefault 作用：与get类似,但可在不含给定键时会返回默认值并更新字典。
        d={};d.setdefault('name','N/A');d;
        #在含有给定键时
        d['name']='zhw';d.setdefault('name','N/A');d

        #11 update 作用：使用一个字典项更新另外一个字典.参数：与dict函数类似.
        
d={'title':'python dict','url':'www.python.org'};x={'title':'zhw dict'};d.update(x);d

        #12 values itervalues 类似于items和iteritems

        
        
