# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 23:12:27 2021

@author: HUAWEI
"""

# 学   号 ：2020211707
# 姓   名 ：谭仁俊
# 开发时间 ：2021/3/2 8:39
#实验任务5
#新建list并输出其长度
classmates = ['Michael' , 'Bob' , 'Tracy']
print(len(classmates))
#查看list中的第一个和第二个元素
print (classmates[0])
print (classmates[1])
#添加元素
classmates.append('Adam')
print(classmates)
#指定位置添加元素
classmates.insert(1,'Jack')
#删除末尾元素
classmates.pop()
print(classmates)
#替换
classmates[1] = 'Sarch'
print(classmates)
#list中存放不同元素类型
L = ['Apple',123,True]
print(L)
#二维数组
s = ['python','java',['asp','php'],'scheme']
print(s)
print(len(s))
#二维数组，内层数组可以用数组变量代替
p = ['asp','php']
s = ['python','java',p,'scheme']
print(s)
#空list长度为0
I =[]
print(len(I))