# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 23:14:04 2021

@author: HUAWEI
"""

# 学   号 ：2020211707
# 姓   名 ：谭仁俊
# 开发时间 ：2021/3/4 13:02
#实验任务7
#新建集合
s =  set([1,2,3])
print(s)
#の集合自动去重
s = set([1,1,2,3,2,3])
print(s)
#添加元素
s.add(4)
print(s)
#删除元素
s.remove(4)
print(s)
#集合の交集和并集
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1&s2)
print(s1|s2)
