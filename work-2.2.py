# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:03:46 2021

@author: HUAWEI
"""
#用python的for循环、列表推导式、分别实现计算1+2+...+1000
range_1=list(range(1,1001))

#列表推导式
print(sum([x for x in range_1]))

#for 循环
sum=0
for i in range_1:
    sum=sum+i
print(sum)
    
