#Excel_test.py
import xlwt,xlrd
import os

#xlwt模块写入数据到excel文件中。
#设置文件路径
excelPath=os.path.join(os.getcwd(),'testdata\\data.xls')
#1.创建excel工作簿workbook
workbook=xlwt.Workbook(encoding='UTF-8')
#2.创建工作簿中的sheet页
sheet=workbook.add_sheet('数据测试单页')
#设置excel标题栏内容
headers=['字段1','字段2','字段3']
#循环写入标题内容
for colIndex in range(0,len(headers)):
    #按照字体格式写入标题
    sheet.write(0,colIndex,headers[colIndex])
#循环写入数据
for rowIndex in range(1,5):
    for colIndex in range(len(headers)):
        sheet.write(rowIndex,colIndex,(rowIndex+colIndex))

#3.保存创建好的excel文件
workbook.save(excelPath)
print('excel文件写入完毕')

#xlrt模块读取excel文件数据

#根据excel路径打开excel文件工作簿
workbook2=xlrd.open_workbook(excelPath)
#获取sheet单页的列表
sheets=workbook2.sheet_names()
#获取第一个单页
worksheet=workbook2.sheet_by_name(sheets[0])
#外层循环获取数据行数
for i in range(0,worksheet.nrows):
    #获取当前行数据
    row=worksheet.row(i)
    #内层循环控制单行的每一列
    for j in range(0,worksheet.ncols):
        #输出当前循环到的cell坐标数据
        print(worksheet.cell_value(i,j),'\t',end=' ')
    print()#用于换行
