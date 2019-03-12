#-*- coding:utf-8 -*-
'''
    douban-book-spider.py
    ---------------------------
    豆瓣图书Top250首页25条信息数据采集

    @copyright: Chiansoft International· ETC
    @author: alvin
    @date: 2018-05-02
'''
# 导入模块
import urllib.request
import re
import json
import os
import logging
import time

# 首先，设置logging日志的基本参数
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fomatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 其次，创建并设置文件处理器FileHandler对象
dirPath = os.path.join(os.getcwd(), 'datatest/log')
if not os.path.exists(dirPath):
    os.mkdir(dirPath)
logFileName = time.strftime('%Y%m%d%H%M%S', time.localtime())+'.log'
logPath = dirPath + os.sep + logFileName
fileHandler = logging.FileHandler(logPath)
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(fomatter)
logger.addHandler(fileHandler)

# 全局变量
content = ''

# 步骤1：设置采集网页的url地址
url = 'https://book.douban.com/top250?icn=index-book250-all'
# 步骤2：使用with语句创建本地程序与网络的链接并获取网页源文件（源代码）
with urllib.request.urlopen(url) as response:
    if response.getcode() == 200:
        content = response.read().decode('utf-8')

# 步骤3：获取采集数据的代码字符串部分，并且设置采集数据的正则表达式
regContent = re.compile(r'<tr class="item">(.*?)</tr>', re.S)
regTitles = re.compile(r'<div class="pl2"><a.*?title="(.*?)">')
regLinks = re.compile(r'<div class="pl2"><a\shref="(.*?)".*?>')
regRatings = re.compile(r'<span class="rating_nums">(.*?)</span>')

# 步骤4：使用findall()函数获取所有的数据代码块
lstContents = regContent.findall(content)

# 步骤5：创建一个列表对象
data = []

for item in lstContents:
    # 代码块字符串处理, 2个以上的空格和所有的换行\n
    regExp = re.compile(r'[\s\n]{2,}')
    blockCode = regExp.sub('', item)
    
    # 创建一个空字典对象，用于封装存放每一个记录的3个数据
    dictBook = {}

    # 获取每一个数据中的图书名称
    lstTitles = regTitles.findall(blockCode)
    bookTitle = lstTitles[0] # 获取当前数据的图书名称
    logger.info(bookTitle) # 日志输出
    dictBook['title'] = bookTitle  # 将数据添加到字典中

    # 获取每一个数据中的图书链接地址
    lstLinks = regLinks.findall(blockCode)
    bookLink = lstLinks[0]
    logger.info(bookLink) # 日志输出
    dictBook['link'] = bookLink  # 将数据添加到字典中

    # 获取每一个数据中的豆瓣评分
    lstRatings = regRatings.findall(blockCode)
    bookRating = lstRatings[0]
    logger.info(bookRating) # 日志输出
    dictBook['rating'] = bookRating  # 将数据添加到字典中

    # 封装好的字典数据添加到list列表中
    data.append(dictBook)
    logger.info('-' * 30)

logging.info(data) # 日志输出

# 步骤6：设置json文件的存储路径
dataDir = os.path.join(os.getcwd(), 'datatest')
if not os.path.exists(dataDir):
    os.mkdir(dataDir)

# 步骤7：将数据写入json文件
with open(dataDir + os.sep +'data.json', 'w', encoding='utf8') as jsonFile:
    # 使用json中的dump()快速序列化并写入指定文件
    json.dump(data, jsonFile, ensure_ascii=False)
    print('>> json文件写入完毕.')
