#集合、堆和双端队列
#也属于数据结构

#1.集合
#set类位于sets模块，python3通过set类型实现，可以直接创建集合。
#集合：顺序是随意的，且副本会被忽略。
#set:参数：序列或其他可迭代对象，主要用于检查成员资格。所以副本会被忽略，下面第二个例子
set(range(10));set([0,1,2,3,0,1,2,3,4,5]);set(['fee','fie','foe'])

#集合方法：并
#并集：使用方法或者使用按位与（or）运算符
a=set([1,2,3]);b=set([2,3,4]);a.union(b);a|b
#判断是否为另一个集合为子集,issubset()方法，或者<=运算符
c=a&b;c.issubset(a);c<=a;
#判断是否为另一个集合为超集，issuperset(另一个集合)，或者>=运算符
c.issuperset(a);c>=a
#交集：使用方法或者使用按位且（and）运算符
a.intersection(b);a&b
#a-b:
a.difference(b);a-b
#不知道什么鬼
a.symmetric_difference(b);a^b
#不了解
a.copy();a.copy() is a

#注意：集合是可变的，不能作为字典的键。
#注意2：集合本身只能包含不可变的值，所以不能包含其他集合。
a=set();b=set();a.add(b)
#所以为了实现集合的集合或者作为字典的键，我们引入forzenset类型：表示不可变的集合；
a=set();b=set();a.add(frozenset(b))


#2.堆
#优先队列的一种。python无独立堆类型，只有一个包含堆操作函数的模块，名为heapq
#heap属性：即位于i位置上的元素总比i/2位置上的元素大（i位置上的元素总比2*i及2*i+1位置上的元素小）
#我们将列表作为堆对象本身--这里的列表要是堆函数建立起来的列表
#heapq模块中重要的函数
heap.heappush(heap,x)           #将x入堆
heap.heappop(heap)              #将堆中最小的元素弹出
heap.heapify(heap)              #将heap属性强制应用到任意一个列表
heap.heapreplace(heap,x)        #将堆中最小的元素弹出，同时将x入堆。
heap.nlargest(n,iter)           #返回iter中第n大的元素
heap.nsmallest(n,iter)          #返回iter中第n小的元素
#注意，heappush()函数不能随意用于列表中，--只能用于通过各种堆函数建立的列表中。
#注意：这里的data需要是一个列表，而非迭代对象。python3的变化。
from heapq import *;from random import shuffle;data=[x for x in range(10)];shuffle(data);heap=[]
for n in data:
    heappush(heap,n)
heap;heappush(heap,0.5);heap
#heappop函数弹出最小元素。
heappop(heap);heappop(heap);heappop(heap)
#注意：heapify函数使用任意列表作为参数--可以将其转换为合法的堆。如果没有用heappush一步步建立堆，那么就要使用heapify将列表转换为合法的堆。
heap=[5,8,0,3,6,7,9,1,4,2];heapify(heap);heap
#heapreplace函数使用
heapreplace(heap,0.5);heap;heapreplace(heap,10);heap

#3. 双端队列
#位于collections模块，包括deque类型
#可通过可迭代对象创建，和一些方法
from collections import deque;q=deque(range(5));
#分别在右端和左端添加元素
q.append(5);q.appendleft(6);q
#分别弹出右端和左端元素
q.pop();q.popleft()
#分别向右移元素，和左移元素。
q.rotate(3);q;q.rotate(-1);q

