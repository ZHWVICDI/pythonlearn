#模块 基础
#模块功能，分析方法，如何使用



#10.1 模块 包，自定义模块导入（3种）。

    #10.1.1 模块即程序 --如何导入自定义目录中的模块（简称编辑sys.path），以及只导入一次机制。
    #告诉解释器，除了从默认目录中寻找要引入模块外，还需要从指定目录寻找模块。

    #1.创建一个python文件hello.py保存在一个目录中。
    #2.指定自定义模块目录
    import sys;
    sys.path.append('D:\python\python_base_practice\python\programs\python模块')
    #然后就可以使用存放在自定义目录的模块了。
    import hello;
    #注意：pyc文件：经过编译的。如果稍后导入同一个模块，python会导入.pyc文件,而不是.py文件。除非.py文件已经改变，就会生成新的.pyc文件。
    #补充：“只导入一次”:为了防止两个模块互相导入会发生无限循环的情况。坚持重新导入模块：reload函数在python3中已被去掉。所以浏览器自己查
    #再次导入hello，不会执行。
    import hello;#没有任何输出。

    
    #10.1.2 模块中用于定义 - 模块中的函数和重用
    #1.模块中定义函数 作用：为了代码重用
    #我们编写一个hello2.py，这里的模块我们仍然放在自定义目录中，然后再里面放置一个hello函数，然后使用它。
    import hello2;hello2.hello()#假设hello为通用函数.
    #2 模块中的测试代码 pass

    #10.1.3 让我们的自定义模块可用
    #10.1.1的例子是一种方法。但我们改变了sys.path的内容，但如果我们需要保证sys.path包含正确的目录。
    #这里有两种方法可以做到：1.我们定义的模块放到正确的位置。2.告诉解释器到哪里去寻找需要的模块，

    #1.将模块放在正确的位置
    #找到正确位置,所打印的每个字符串目录提供了放置模块的目录，解释器从这些目录中找所需要的模块。顺序为默认-》自定义
    #site-packages目录是最佳选择。这里我们将another_hello,py文件放在该目录中，然后测试。
    import sys,pprint;pprint.pprint(sys.path);import another_hello;another_hello.hello()

    #2.告诉解释器到哪儿去找
    #除却编辑sys.path 还有就是在PYTHONPATH环境变量中包含模块所在的目录。pass

    #10.1.4 包--另一种模块，可以包含其他模块（组织模块的作用）。必须包含名为__init__.py的文件。也可作为普通模块导入。
    #包组织模块：将模块放入包目录内即可。
    #创建drawing的包，包含shapes和colors模块。
    #引用包和模块,当然我们仍然要将目录添加入sys.path中去。
    import drawing;import drawing.colors;from drawing import shapes
    
#10.2   探究模块-如何快速理解网上的模块，1个技能。
    
    #10.2.1 模块的内容。
    #我们先导入，然后在解释器中研究它。
    #这里我们研究copy模块,先导入。
    import copy
    #1. dir函数：列出对象（以及模块的所有函数、类、变量等）的所有特性。参数：对象名或模块名
    #列表推导式加dir输出不以下划线开头的名字的列表。
    [n for n in dir(copy) if not n.startswith('_')]

    #2. __all__变量 ：定义了模块的公有接口。也是在from copy import *中*的内容。
    #小技巧：在编写模块时设置__all__。可以过滤掉很多不需要的变量。未设定__all__，import *语句默认输出模块中不以下划线开头的全局名称。

    
#10.2.2 help获取帮助
    
help(copy.copy)
    #__doc__:获取文档字符串；相比help，help具有更多的信息。

    #10.2.3 文档
    #除了__doc__文档字符串，就是标准python库参考。网址：http://python.org/doc/lib

    #10.2.4 源代码 阅读源代码，学习的方式
    #这里我们希望阅读标准模块copy的源代码，如何找到呢
    #1.检查sys.path，然后自己去找。2.检查__file__属性：然后查看即可

#10.3 标准库 这里单独列出来，每个模块结合ppt以及代码来学习。
    
    
    
