# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 23:16:41 2021

@author: HUAWEI
"""
# 学   号 ：2020211707
# 姓   名 ：谭仁俊
# 开发时间 ：2021/3/4 20:58
#实验任务9
#英文字符串，计算位数
print(len('ABC'))
#中文字符串，计算位数
print(len('中文'))
#查看bytes类型の数据’ABC‘的字节数
print(len(b'ABC'))
#查看一个bytesの字节数
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
#查看中文被’utf-8'编码后的位数
print(len('中文'.encode('utf-8')))

#字符串格式化输出
print('Hello,%s' % 'world')
print('Hi,%s,you have $%d.' % ('Michael',1000000))
