#re 模块
#1.正则表达式:可以匹配文本片段的模式。

#注意特殊字符表示普通文本意思的时候要转义

#.:通配符，匹配除换行符外的任何单个字符。
#转义：pass
#字符集：匹配包含的任意字符
    #1.中括号括住字符串创建字符集。
    [py]ython#匹配python和jython
    #2.使用范围匹配
    [a-z]   #匹配a到z的任意一个字符
    #3范围联合使用
    [a-zA-Z0-9] #匹配任意大小写字母和数字，单个。
    
#反转字符集
    [^abc]      #匹配任何除了a、c和b之外的字符
#选择符和子模式
    #使用管道符号|即选择符
    python|perl #匹配python或者perl
    
#子模式：即下面圆括号括起来的部分
    p(ython|erl)   #匹配python或者perl
#可选项和重复子模式
    #可选项：子模式后加上问号，表示可选
    r'(http://)?(www\.)?python\.org'#匹配四个，你懂的
    #重复子模式：
        (pattern)*:表示允许模式重复0次或多次
        (pattern)+:1或多次
        (pattern){m,n}:m-n次
#字符串的开始和结尾
    #^，字符串开始
    ^ht+p  #只会在字符串开头匹配
    #$,字符串结尾匹配

#2.re模块的内容
#re模块中的重要函数
import re
re.compile(pattern[,flags])         #根据包含正则表达式的字符串创建模式对象(也即是正则表达式对象)。
    #当我们需要重复使用该正则表达式的时候，使用它
    #!!!!模式对象本身具有查找/匹配的函数，就像方法一样，所以re.search(pat,string)等价于pat.search(string)。
re.search(pattern,string[,flags])   #在字符串中寻找模式？？？；功能：在给定的字符串中寻找第一个匹配正则表达式的子字符串。返回值：找到返回MatchObject，否则返回None
    if re.search(pat,string):
        print('Found it!')
re.match(pattern,string[,flags])    #在字符串开始处匹配模式
    re.match('p','python');re.match('p','cop');
    #注意：如果要匹配整个字符串在模式末尾加上$符号
    re.match('cop$','coppat')
re.split(pattern,string[,maxsplit=0])   #更具模式的匹配项来分割字符串,返回值：列表
    #使用split用任意长度的逗号和空格序列来分割字符串
    some_text='alpha, beta,,,gamma delta';re.split('[, ]+',some_text)
    #参数maxsplit:表示字符串最多可以分割的部分数
    re.split('[, ]+',some_text,maxsplit=2)
re.findall(pattern,string)          #列表形式返回字符串中模式的所有匹配项
    pat='[a-zA-Z]+';text='"Hm..Err--are you sure?" he said , sounding insecure';re.findall(pat,text)
re.sub(pat,repl,string[,count=0])   #将字符串中所有pat的匹配项用repl替代
    #替换
    pat='{name}';text='Dear {name}';re.sub(pat,'Mr,zhw',text)
re.escape(string)                   #将字符串中所有的特殊正则表达式字符转义
    #当字符串很长且包含很多特殊字符，而我们不想输入大堆反斜线或字符串来自用户，要做为正则表达式的时候
    re.escape('www.python.org')
#经过compile和一般正则表达式的区别：使用compile返回模式对象会更有效率。使用普通正则表达式时，serach或者match函数仍然会转换其为模式对象
#注意：模式对象本身具有查找/匹配的函数。

#3 匹配对象和组
#MatchObject对象：对于re模块中队字符串进行模式匹配的函数，当能找到匹配项时，会返回该对象。包含匹配模式的子字符串的信息。且包含哪个模式匹配子字符串哪部分的信息。这些部分称为组。
#组：就是放置在圆括号内的子模式,所以组是相对于正则字符串来说的。组的序号取决于左侧括号数。组0表示整个模式
#例如'There (was a (wee)(copper)) who (lived in Fyfe)'从左到右
#组的作用：我们有时候对给定组的内容感兴趣，可以提取出来

#匹配对象的重要方法（参数就是组号）
MatchObject.group([group1,...])    #获取给定子模式的匹配项.未给定组好，默认为组0，给定组号，返回单个字符串。
MatchObject.start([group])          #返回给定组匹配项的开始位置
MatchObject.end([group])            #返回给定组的匹配项的结束位置
MatchObject.span([group])           #返回一个组的开始和结束位置
#例子
m=re.match(r"www\.(.*)..{3}",'www.python.org');m.group(1);m.start(1);m.end(1);m.span(1)


#4 作为替换的组号和函数
#re的sub函数和组号合用
    #提供一个正则表达式
    emphasis_pattern=r'\*([^\*]+)\*'
#补充：在re中使用VERBOSE标志使得正则表达式更加易读。允许模式中添加空白
#下面这个和上面等价
emphasis_pattern=re.compile(r'''
    \*
    (
    [^\*]+
    )
    \*
    ''',re.VERBOSE)

re.sub(emphasis_pattern,r'<em>\1</em>','Hello,*world*!')
#补充：贪婪模式和非贪婪模式
#贪婪模式：尽可能多的据为己有，多多益善--这里指内容而不是匹配数目。
emphasis_pattern=r'\*(.+)\*';re.sub(emphasis_pattern,r'<em>\1</em>','*This* is *it*!')
#非贪婪模式:下面的是模式用+？替代了+，表示非贪婪模式。尽可能少的匹配。
emphasis_pattern=r'\*\*(.+?)\*\*';re.sub(emphasis_pattern,r'<em>\1</em>','**this** is  **it**')



