#EXCEL文件的读写
#外部模块 xlrd xlwd
#xlrd:读取excel文件模块
#xlwt：写入excel文件模块

#excel文件操作的两个重要对象workbook（工作簿）和sheet(单页)


#excel文件写入的标准操作：
    #1.获取excel文件的绝对路径
    #2.创建工作簿workbook
        #函数：xlwt.Workbook(encoding=字符编码集)：返回值：workbook对象
    #3.工作簿中创建sheet单页
        #函数：workbook对象.add_sheet(sheet单页的名称)：返回值：sheet对象
    #4.添加数据
        #函数：sheet对象.write(行下标，列下标，数据值)
    #5.保存工作簿workbook
        #函数：workbook对象.save(excel文件绝对路径)
