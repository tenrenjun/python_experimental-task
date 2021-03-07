# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 23:13:32 2021

@author: HUAWEI
"""

# 学   号 ：2020211707
# 姓   名 ：谭仁俊
# 开发时间 ：2021/3/2 9:02
#实验任务6
#新建字典
d = {'Michael':95,'Bob':75,'Tracy':85 }
print(d['Michael'])
#添加元素
d['Adam']=67
print(d['Adam'])
d['Jack']=90
print(d['Jack'])
#
d['Jack']=88
print(d['Jack'])
#用三种方式判断'Thomas"是否为d的一个key
print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas',-1))
#删除元素
d.pop('Bob')
print(d)