# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:37:13 2021

@author: HUAWEI
"""
import numpy as np 
import pandas as pd

#用于返回将字典转化为dataframe类型数据，行索引为ABCDEFGHIJ,列索引为abcde
d = {'a' : pd.Series(np.random.randn(10), index=['A','B','C','D','E','F','G','H','I','J']),
     'b' : pd.Series(np.random.randn(10), index=['A','B','C','D','E','F','G','H','I','J']),
   'c' : pd.Series(np.random.randn(10),  index=['A','B','C','D','E','F','G','H','I','J']),
   'd' : pd.Series(np.random.randn(10),  index=['A','B','C','D','E','F','G','H','I','J']),
   'e' : pd.Series(np.random.randn(10),  index=['A','B','C','D','E','F','G','H','I','J']),}
df = pd.DataFrame(d)
print(df)
df.plot.bar()
df.plot.box()
df.plot(colormap='gist_rainbow').scatter(x='a',y='b')
df.plot.hexbin(x='a',y='b')
#对生成的一系列随机数的series数据类型绘制饼图
df1 = pd.Series( 5 * np.random.rand(10),index=['A','B','C','D','E','F','G','H','I','J'],name='series')
print(df1)
df1 .plot.pie(figsize=(10,10))
#int
df2 = pd.DataFrame(np.random.randint(0,5,size=(10,5)),columns=['a','b','c','d','e'])
print(df2)
df2.plot.line()