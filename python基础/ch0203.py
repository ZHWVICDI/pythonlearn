#序列 每个元素具有一个位置，即索引

#2.1python包含6种内建序列 ：列表，元祖， 字符串，Unicode字符串，buffer对象，xrange对象。
#列表和元组的主要区别：列表可修改，元组不可修改。
#注意：python中，序列、映射以及集合组成容器，内建序列6种。序列每个元素具有索引，映射每个元素具有一个键。

#2.2通用序列操作 ：索引、分片、加、乘、以及成员资格（还有迭代）。python内建函数：计算序列长度、找出最大元素和最小元素。

    #2.2.1 索引
    #序列通过编号，字典通过键。
    greeting='Hello';
    greeting[0]
    #使用负数索引,从右向左-1开始
    greeting[-1]
    #字符串字面值直接使用索引
    'Hello'[1]
    #直接对返回结果进行索引操作
    fourth=input('Year:')[3];
    fourth
    #索引实例见ch01_index.py
    
    #2.2.2 分片
    tag='<a href="http://www.python.org">Python web site</a>';
    tag[8:30];
    tag[32:-4]
    #分片格式 序列[第一个索引:剩下部分的第一个索引:步长] 第一个索引的元素包含在内，剩下部分的第一个索引的元素不包含在内。
    numbers=[1,2,3,4,5,6,7,8,9,10];
    numbers[3:6]
        #1.优雅的捷径
        #只要分片中最左边的索引比右边的在序列中的位置靠右，结果为一个空序列。
        numbers[-3:0]
        #访问序列结尾部分的元素
        numbers[-3:]
        #访问序列开始部分的元素
        numbers[:3]
        #访问整个序列
        numbers[:]
        #分片实例详见ch01_fenpian.py 对指定格式的URL进行分割
        #2.更大的步长
        #步长指定为2
        numbers[0:10:2]
        numbers[::4]
        #步长可以为负数,即从右向左提取元素
        numbers[8:3:-1]#同样的第一个索引的元素包含在内，第二个索引不包含在内
        numbers[0:10:-2]#这里为空序列，因为第一个索引在第二个元素的左边。这里和正步长相反。记忆方法：箭头法，两索引所构成箭头指向正确方向即可，正步长，箭头从左到右。

    #2.2.3 序列相加 :通过+号对相同类型的序列进行连接操作
    [1,2,3]+[4,5,6];
    'Hello,'+'world!';

    #2.2.4 乘法
    #数字乘以一个序列来生成一个新的原序列被重复x次的序列
    'python'*5;
    [42]*10
        #None、空列表和初始化
        #None;Python的内建值，表示空值（什么都没有可放置任何元素）
        #初始化长度为10的列表
        sequence=[None]*10;
        sequence
     #序列乘法实例见ch02_wordsinbox.py 用于在‘盒子中打印句子’

    #2.2.5 成员资格
    # in运算符：用于检查一个值是否在序列中，返回布尔值。
    permissions='rw';'w'in permissions;'x' in permissions
    users=['mlh','foo','bar'];input("enter your name:")in users #用于权限检查
    subject='$$$ Get rich now!! $$$';'$$$'in subject
    #序列成员资格实例见ch02_access.py

    #内建函数 len、min、max
    numbers=[100,34,678]
    #len函数返回序列中包含的元素数量
    len(numbers)
    #min、max函数返回序列中最大和最小的元素
    max(numbers);min(numbers)


#2.3 列表：python的苦力,可变
    

    #2.3.1 list函数
    #根据字符串创建列表。不限于字符串，所有类型的序列都可以。
    list('Hello')
    #将字符组成的列表转换为字符串
    somelist=['H','e','l','l','o'];''.join(somelist)
    
    #2.3.2 基本的列表操作
    #列表可使用所有适用于序列的标准操作：索引，分片，加，乘，成员资格。
    #改变列表的方法：元素赋值，元素删除，分片赋值以及列表方法。有些不真正的改变列表
        #1. 改变列表：元素赋值
        #索引标记为某个元素赋值
        x=[1,1,1]; x[1]=2; x#注意不能为位置不存在的元素进行赋值
        #2.删除元素 del del也可用于字典等的删除操作
        names=['Alice','Beth','Cecil','Dee-Dee','Earl'];del names[2];names
        #3.分片赋值
        name=list('Perl');name;name[2:]=list('ar');name
        #使用不等长的序列替换分片
        name[1:]=list('ython');name
        #不替换任何原有元素的情况下插入新的元素
        numbers=[1,5];numbers[1:1]=[2,3,4];numbers
        #删除元素
        numbers[1:4]=[];numbersrs
        
    #2.3.3 列表方法
    #方法的调用方式：对象.方法(参数)
        
        #1. append  作用：用于在列表末尾追加新的对象。参数：一个对象。返回值：无返回值而是修改了原列表的内容。
        lst=[1,2,3];lst.append(4);lst
        #2. count   作用：统计某个元素在列表中出现的次数。参数：某个元素。返回值：元素出现的个数。
        ['h','h','h'].count('h');
        #3. extend  作用：在列表的末尾追加另一个序列的多个值。参数：一个序列。返回值：无返回值而是修改原列表
        a=[1,2,3];b=[4,5,6];a.extend(b);a
        #注意:这与连接操作很相似，两者最主要的区别：extend方法修改原列表，而连接操作返回一个全新的列表。
        a=[1,2,3];b=[4,5,6];a+b;a
        #有时连接操作的效率比extend方法低
        a=a+b        
        #分片赋值实现连接
        a=[1,2,3];b=[4,5,6];a[len(a):]=b;a
        #4. index    作用：在列表中找出某个值第一个匹配项的索引位置。参数：某个元素。返回值：第一个匹配项所在位置。
        knights=['We','are','the','knights','who','say','ni'];knights.index('who');
        #5. insert   作用：将对象插入到列表中。参数：1.插入位置。2.插入对象。
        numbers=[1,2,3,4,5,6,7];numbers.insert(3,'four');numbers
        #分片赋值实现insert
        numbers=[1,2,3,5,6,7];numbers[3:3]=['four'];numbers
        #6. pop      作用：移出列表的最后一个元素。参数：可以为索引。返回值：返回元素的值。
        x=[1,2,3];x.pop();x;x.pop(1);x
        #使用pop和append方法来实现栈的数据结构
        x=[1,2,3];x.append(x.pop());x
        #栈的实现：pop出栈，append入栈。队列的实现：insert(0,...)入队列，pop()出队列。当然，更好的方法是使用collection模块中的deque对象。
        #7. remove   作用：移除列表中某个值的第一个匹配项。参数：列表中元素。返回值：无返回值而修改了源列表。
        x=['to','be','or','not','to','be'];x.remove('be');x;x.remove('to');x        
        #8. reverse  作用：反向存放列表中的元素。参数：无。返回值：无而改。
        x=[1,2,3];x.reverse();x
        #提示：对一个序列进行反向迭代，使用reversed函数。
        x=[1,2,3];list(reversed(x));
        #9. sort     作用：在原位置对列表进行排序（原位置排序表示改变原来的列表，而不是返回一个排序的列表副本）。参数：可选 key和reverse。返回值：无但改。
        x=[4,6,2,1,7,9];x.sort();x;
        #需要一个排序的列表副本时，而不希望原列表改变。
        x=[4,6,2,1,7,9];y=x[:];y.sort();x;y#我们先赋值给副本，再对副本排序。        
        #使用sorted函数，获取排序的列表副本。
        x=[4,6,2,1,7,9];y=sorted(x);x;y
        #10. 高级排序 cmp sort方法和sorted函数的key以及reverse可选参数
        #cmp:内建函数，提供默认的比较函数实现方式.这个版本好像没有？
        cmp(42,32);cmp(99,100);cmp(10,10);numbers=[5,2,9,7];numbers.sort(cmp);numbers
        #sort方法的可选参数--key和reverse。
        #key：为每个元素创建一个键（键函数），然后所有元素根据键来排序。列子根据元素长度来排序。
        x=['aaad','abalone','camsdfsdfsde','adsdfddd'];x.sort(key=len);x
        #reserve参数:简单的布尔值，指明列表是否进行反向排序。
        x=[4,6,2,1,7,9];x.sort(reverse=True);x


#2.4  元组：不可变序列
#创建元组：用逗号分隔一些值，就自动创建了元组。
1,2,3
#圆括号括起来
(1,2,3)
#空元组：
()
#一个值的元组，必须要加个逗号。所以对于一个元组，逗号是重要的。
42;42,;(42,)#后两个是对的

    #2.4.1 tuple函数
    #类似于list函数。将一个序列作为参数并转换为元组。
    tuple([1,2,3]);tuple('abc')

    #2.4.2 基本元组操作
    #类似于列表，元组分片还是元组，列表分片还是列表。因为元组不可变，所以不适用列表的有些方法和基本操作。

    #2.4.3 元组的不可替代性
    #元组可以在映射(或集合)中当作键使用。
    #元组可作为很多内建函数和方法的返回值存在。

#3  字符串
#字符串格式化，分割，链接，搜索。
    

    #3.1 基本字符串操作
    #所有的序列标准操作对字符串都适用。字符串不可变。因此不可使用有些分片赋值，

    #3.2 格式化字符串格式化
    # % 来实现，这个类似于c语言。python中，格式为：格式化字符串 % 格式化的值。这个值可以是一个字符串或数字，或元组或字典。这里如果使用列表或其他序列，则只会被解释为一个值。
    format="%s,%s,you are lovers!";values=("zhw","tyq");print(format % values)
    # %s ：转换说明符，该值格式化为一个字符串，如果不是字符串则用str将其转换为字符串。
    # 注意：格式化字符串中出现%号用%%来转义。
    # %f :格式化浮点数。格式：.希望保留的小数位数f
    format="Pi with three decimals:%.3f";from math import pi;print(format % pi);
    #string模块的模块字符串。
    from string import Template;s=Template('$x,glorious $x!');s.substitute(x='slurm');
    #$$ 在模块字符串中插入美元符。
    #用字典变量为模块字符串提供值/名称对。
    s=Template('A $thing must never $action.');d={};d['thing']='gentleman';d['action']='show his socks';s.substitute(d)
    #替换字段为单词的一部分时。参数名用括号括起来。
    s=Template("It's ${x}tastic!");s.substitute(x='slurm');

    #3.3 字符串格式化完整
    #当%右操作数为元组时，每个元素单独格式化，每个值都需要一个对应的转换说明符。
    #基本的转化说明符
        #（1）%字符：开始
        #(2) 转换标志（可选）：-表示左对齐；+表示转换值前要加正负号；”“（空白字符）表示正数前保留空格；0表示转换值位数不够用0填充。
        #(3) 最小字段宽度（可选）：转换后的字符串至少具有该值指定的宽度。为*时，宽度从值元组中读出。
        #(4) . 后跟精度值（可选）：转换的是实数，精度值表示小数点后的位数。转换的是字符串，表示最大字段宽度。为*时，精度从元组中读出。
        #(5) 转换类型 ：d,i 带符号十进制；o不带符号的八进制；u 不带符号的十进制；x不带符号的十六进制（小写）;X (大写);e及E 科学计数法表示的浮点数;f,F 十进制浮点数；g和G 指数大于-4或小于精度值与eE同，否则和fF同；C 单字符；s 字符串。
    
        #3.3.2 字段宽度和精度
        #字段宽度：转换后的值所保留的最小字符个数。精度：同上,对于字符串则是最大字符宽度。
        #字段款为10
        from math import pi;'%10f' % pi
        #精度为2
        '%.5s' % 'Guido van Rossum'

        #3.3.3 符号、对齐和0填充
        #标表：可以为0、+、-、空格
        '%010.2f' % pi
        #(-)来左对齐数值
        '%-10.2f' % pi
        #空白：表示在正数前加上空格来填充。用于对齐正负数时。这里就是右对齐
        print('% 5d' % 10+'\n' +('% 5d' % -10))
        #字符串格式化实例见ch02_strTo.py
    
    #3.4 字符串方法    
    #全部方法参见附录B
    #有用的字符串常量：
        string.digits#包含数字1~9的字符串。
        string.letters#包含所有字母的字符串。在python3中应使用string.ascii_letters
        string.lowercase#包含所有小写字母的字符串。
        string.printable#包含所有可打印字符
        string.puctuation#包含所有标点。
        string.uppercase#包含所有大写字母.
        
        #3.4.1 find方法 作用：在较长字符串中查找子字符串。参数：子字符串，可选的起始点和结束点参数。返回值：子串所在位置最左端索引,否则返回-1.
        'With a moo-moo here,and a moo-moo there.'.find('moo')
        #这里in好像也可以胜任
        'moo'in'Width a moo-moo here,and a moo-moo there.'#结果为True
        #提供起始点,注意这里是包含第一个索引，不包含第二个索引。
        subject='$$$ Get rich now!!! $$$';subject.find('$$$');subject.find('$$$',1);subject.find('!!!',0,16)
        #3.4.2 join方法 作用：在队列中添加元素（需要添加的元素必须是字符串）.参数：返回值：字符串。
        #该逆方法为split
        seq=[1,2,3,4,5];sep='+';sep.join(seq);
        seq=['1','2','3','4','5'];sep.join(seq);
        dirs='','usr','bin','env';'/'.join(dirs);print('C:'+'\\'.join(dirs))#这里与文件结合
        #3.4.3 lower 作用：返回字符串小写版
        'Taondhein Hammer Dance'.lower()
        #'编写不区别大小写'的代码时,在存储和搜索时都转换为小写。
        names=['gumby','smith','jones'];name='Gumby';
        if name.lower() in names:print('found!');
        #title方法 作用：将字符串转化为标题格式（即每个单词首字母大写，而其他字母小写。）
        "that's all folks".title()
        #string 模块的capwords函数
        import string;string.capwords("that's all ,folks")
        #3.4.4 replace 作用：返回某字符串所有匹配项均被替换后的字符串。
        'This is a test'.replace('is','eez')
        #3.4.5 split 作用：将字符串分割为序列。返回值：列表
        '1+2+3+4+5'.split('+');#'+'号可以指定，默认为空格作为分隔符（空格、制表、换行）
        #3.4.6 strip 作用：返回去除两侧空格的字符串。（不包括内部）
        ' lksjdlfjas  ;ldfjaslfj  asldfj '.strip()
        #指定需要去除的字符
        '*** SPAM * for * everyone!!! ***'.strip(' *!')
        #3.4.7 translate 作用：替换字符串中的某些部分：
        #translate和replace区别：translate只能替换单个的字符，但是可以同时进行多个的替换，效率优势。
        #暂且掠过。。。。。。。。。。。。

        
        
        
        
        
        
        
        

    
        
