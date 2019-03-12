import pickle,os
from io import BytesIO
#员工类
class Employee():
    #构造方法
    def __init__(self,empno,ename):
        self.__empno=empno
        self.__ename=ename
        pass
    #对象输出
    def __str__(self):
        print('empno:{0}'.format(self.__empno))
        print('ename:{0}'.format(self.__ename))
        return ''

#员工操作类
class EmployeeDao():
    def __init__(self):
        pass
    def addEmployee(self,employee,filePath):
        with open(filePath,'wb') as fp:
            pickle.dump(employee,fp)
            print('提示：员工添加成功。')
            pass
    def findAllEmployee(self,filePath):
        with open(filePath,'rb') as fp:
            #使用load(读取)
            data=pickle.load(fp)
            print(data)
#脚本入口            
if __name__=='__main__':
    filePath=os.path.join(os.getcwd(),'testdata')
    print("#"*30)
    print("添加员工信息：")
    print('#'*30)
    empno=input('empno:')
    ename=input('ename:')
    emp=Employee(empno,ename)
    empDao=EmployeeDao()
    #实现对象持久化存储
    empDao.addEmployee(emp,filePath+os.sep+'employee.info')
    #反序列化获取对象
    empDao.findAllEmployee(filePath+os.sep+'employee.info')
    #补充：StringIO和BytesIO
    #也就是在内存中读写

    #StringIO()：创建内存空间并写入字符串数据str
    #BytesIO()：创建内存空间并写入字节数据Bytes
    
    #创建内存空间
    f=BytesIO()
    #写入字节数据操作，这里我们写入序列化后的对象emp
    f.write(pickle.dumps(emp))
    #读取字节数据操作，这里我们从内存空间获取我们写入的对象
    e=f.getvalue()
    print(e)
    #然后我们反序列化该对象
    e=pickle.loads(e)
    print(e)
    pass
    


