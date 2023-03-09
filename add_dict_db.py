"""
初始数据库 向数据库写入字段数据
"""

from mysql_rw import *

wdb = Database_rw()  # 创建数据库操作对象
wdb.create_cur()     # 创建游标对象

with open('dict.txt','r') as f:
    # 循环读取字典每一行
    for line in f:

        # 获得 单词 和 解释
        data = line.split(' ',1)       # 以第一个空格分割字符串
        word = data[0]                 # 单词是第一个元素
        # print('word:',word)
        mean = data[1].lstrip()[:-1]   # 第二个元素是解释 去掉左边空格和结尾换行符
        # print('mean:',mean)

        # # 调用模块的添加函数 讲数据写入数据库
        wdb.insert_into_table(('word','mean'),(word,mean),table='words')

wdb.close()




