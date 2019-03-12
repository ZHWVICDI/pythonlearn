#简单数据库

#使用人名作为键的一个字典，每个人用另一个字典表示，其键'phone'和'addr'表示电话号码和地址

people={
    'Alice':{
        'phone':'2341',
        'addr':'Foo drive 23'
        },
    'Beth':{
        'phone':'9102',
        'addr':'Bar street 42'
        },
    'Cecil':{
        'phone':'3458',
        'addr':'Baz avneue 90'
        }
    }


#针对电话号码和地址使用的描述性标签，打印输出时使用
labels={
    'phone':'phone number',
    'addr':'address'
    }

name=input('Name:')
request=input('Phone number(p) or address(a)?')


#查找电话号码或者地址？使用正确的键：

#使用正确的键，用户输入转换为内部的key：
if request=='p':key='phone'
if request=='a':key='addr'

#名字为字典中有效键时才打印信息
if name in people:print("%s's %s is %s." % \
                        (name,labels[key],people[name][key]))
