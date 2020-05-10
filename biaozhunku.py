# import os   #导入os库
#
# print(os.listdir())     #以列表形式展示文件夹下的文件
# print(os.getcwd())      #打印当前路径
#
# print(os.path.exists("b"))  #判断当前路径下有没有文件b。返回True有、Flase没有
# if not os.path.exists("b"):#如果b文件夹不存在
#     os.mkdir("b")#在当前路径下新建文件夹b
# if not os.path.exists("b/test.txt"):#如果b/test.txt文件不存在
#     f = open("b/test.txt","w")
#     f.write("hello,os using!")
#     f.close()

# import time #导入time库
#
# print(time.asctime())
# print(time.time())
# print(time.localtime())
# def strftime(format,p_tuple=None):
#     pass
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# #获取2天前、3天后的时间
# now_time = time.time()
# tow_day_before_time = now_time - 60*60*24*2
# three_day_after_time = now_time + 60*60*24*3
# time_tuple1 = time.localtime(tow_day_before_time)
# time_tuple2 = time.localtime(three_day_after_time)
# print(time.strftime("%Y-%m-%d %H:%M:%S",time_tuple1))
# print(time.strftime("%Y-%m-%d %H:%M:%S",time_tuple2))

# import urllib.request
# response = urllib.request.urlopen("https://www.baidu.com")
# print(response.status)
# print(response.read())

import math

print(math.ceil(5.5))    #返回≥x的最小整数
print(math.floor(5.5))      #返回x的下限整数
print(math.sqrt(6.25))        #计算x的平方根

