# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 23:09:56 2021

@author: HUAWEI
"""

# 学   号 ：2020211707
# 姓   名 ：谭仁俊
# 开发时间 ：2021/3/4 21:20
#实验任务14
'plot'
import pandas as pd
import numpy as np
'饼图绘制'
#对生成的一系列随机数的series数据类型绘制饼图
df1 = pd.Series(3 * np.random.rand(4),index=['a','b','c','d'],name='series')
df1 .plot.pie(figsize=(6,6))
'柱状图绘制'
#对生成的四列随机数的DataFrame数据类型绘制柱状图
df2 = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df2.plot.bar()
'箱线图绘制'
#对生成的五列随机数的dataframe的数据类型绘制箱线图
df3 = pd.DataFrame(np.random.rand(10,5),columns=['a','b','c','d','e'])
df3.plot.box()
'散点图绘制'
#对生成的四列随机数的dataframe数据类型绘制散点图
df4 = pd.DataFrame(np.random.rand(50,4),columns=['a','b','c','d'])
df4.plot.scatter(x='a',y='b')

