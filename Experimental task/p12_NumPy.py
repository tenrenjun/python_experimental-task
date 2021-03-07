# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 23:18:31 2021

@author: HUAWEI
"""

'实验任务12'

###NumPy的教程###
import numpy as np

"random 函数使用"
#用于返回指定size=1的随机数
print(np.random.random(size=1))
#用于返回指定size=2的随机数
print(np.random.random(size=2))
#用于生成[-5,0]的3*2的随机数组
print(np.random.random_sample((3,2))-5)

"array 函数使用"
#用于返回1行3列的整形数组
print(np.array([1,2,3]))
#用于返回1行3列的浮点数数组
print(np.array([1,2,3.0]))
#用于从numpy的矩阵子类返回2行2列的数组
print(np.array(np.mat('1 2; 3 4'))) 

"arange 函数使用"
#用于返回0到3的整数数组(不包含3)
print(np.arange(3))
#用于返回3到7的浮点数数组(不包含7.0)
print(np.arange(3,7.0))
#用于返回3到7的间隔为2 的数组（不包含7）
print(np.arange(3,7,2))