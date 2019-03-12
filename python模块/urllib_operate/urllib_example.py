#urllib_example.py
import urllib.request,threading
import os,sys

#创建一个线程类
class DownloadThread(threading.Thread):
    def __init__(self,url,savePath,fileName):
        threading.Thread.__init__(self)
        self.__url=url
        self.__savePath=savePath
        self.__fileName=fileName
        pass
    def run(self):
        os.system('cls')
        #输出信息
        print('下载文件基本信息：')
        print('-'*40)
        print('文件名称：{0}'.format(self.__fileName))
        #获取远程文件的基本数据1
        fileType=self.__fileName.split('.')[-1]
        print('文件类型:{0}'.format(fileType))
        #计算远程文件的大小
        #使用urllib.request.urlretrieve()函数获取headers信息
        local_filename,headers=urllib.request.urlretrieve(self.__url)
        #获取文件大小值
        contentLength=int(headers['Content-Length'])
        print('文件大小：{0}'.format(contentLength))
        print('下载路径:{0}'.format(self.__url))
        print('保存路径：{0}'.format(self.__savePath))
        print('-'*40)
        print('[启动]>>>{0}文件启动下载....'.format(self.__fileName))
        #使用urlretrieve(资源地址，保存路径，过程回调)函数实现文件下载
        urllib.request.urlretrieve(self.__url,savePath,schedule)
        print('Download progress:100%')
        print('[完成]>>>{0}文件下载完毕'.format(self.__fileName))
        pass
    pass

#这里是按照urlretrieve的参数要求的，用于被urlretrieve回调，自动的，我们不需要提供参数。
def schedule(block,blocksize,contentLength):
    '计算并显示下载进度'
    #block:已经下载的数据块大小
    #blocksize:数据块的大小
    #contentLength:远程文件的大小
    #计算下载的百分比
    per=100.0*block*blocksize/contentLength
    if per>100:
        per=100
        #同一位置输出数据
        sys.stdout.write('Download progress:%.2f%% \r'%(per))
        sys.stdout.flush()
        pass

#脚本入口调用、
if __name__=='__main__':
    #获取远程文件的基本数据
    #设置网络资源地址
    url='http://www.python.org/ftp/python/2.7.5/python-2.7.5.tar.bz2'
    fileName=url.split('/')[-1]
    #设置下载保存路径
    savePath=os.path.join(os.getcwd(),'datatest'+os.sep+fileName)
    #创建下载线程
    downloadThread=DownloadThread(url,savePath,fileName)
    #启动该线程
    downloadThread.start()
    downloadThread.join()
