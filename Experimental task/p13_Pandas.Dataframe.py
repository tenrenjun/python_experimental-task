# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 23:19:28 2021

@author: HUAWEI
"""
"实验任务13"

###pandas的使用教程###
import pandas as pd
import numpy as np

'Series 使用'
#用于返回行索引为abcde的随机数的series类型数据
s = pd.Series(np.random.randn(5), index=['a','b','c','d','e'])
print(s)
#用于返回将字典类型数据强制转化为series类型数据
d = {'a' : 0., 'b' : 1., 'c' : 2.}
print(pd.Series(d))

'DataFrame 使用'
#用于返回将字典转化为dataframe类型数据，行索引为abcd,列索引为one,two
d = {'one' : pd.Series([1.,2.,3.], index=['a','b','c']),
    'two' : pd.Series([1.,2.,3.,4.],index=['a','b','c','d'])}
df = pd.DataFrame(d)
print(df)
#用于返回dataframe数据类型的行索引
print(df.index)
#用于返回dataframe数据类型的列索引
print(df.columns)
