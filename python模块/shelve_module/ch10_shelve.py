#shelve 模块
#提供一个简单的存储方案，只需提供一个文件名
#open函数：返回值：一个shelf对象，可以用来存储内容。只需要将其当作普通的字典（但是键一定要是字符串）来吃操作即可，完成工作后，调用close方法

#1.潜在的陷阱
import shelve;
#注意不要自己创建dat文件，回报错误。
s=shelve.open(r"D:\python\python_base_practice\python\programs\python模块\shelve_module\testfuckyou.dat");
#这里不会打印d，因为shelf对象根据已存储的版本进行构建，当将元素赋给某个键时，对象被存储。
s['x']=['a','b','c'];s['x'].append('d');s['x']
#所以，当我们赋值给s时，就会存储一下。然后是获取存储表示，来创建一个新的列表，‘d’就是被添加到这个副本中。而修改的版本没有被存储。所以获取的是原始的版本。

#解决方案1:讲临时变量绑定到获取的副本上，然后修改后重新存储该副本。
temp=s['x'];temp.append('d');s['x']=temp;s['x']
#总之：我们总是先赋值给临时变量，在临时变量上进行更改，最后赋值回s即可。

#解决方案2：open函数有个可选参数writeback设为true，这样所有从shelf读取或赋值的操作都会保存在内存中，只有在关闭shel的时候才写回。//限于数据不大时。


