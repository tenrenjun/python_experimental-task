# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:06:16 2021

@author: HUAWEI
"""
#用python实现F1-score，并创建一个简单数据集进行测试

# F1-score 实现 
import numpy as np 
# 构建的简易数据集： 
# 实际数据的标签（其中 0 表示反例，1 表示正例） 
date_true = np.random.randint(0, 2, 5000) 
date_true = date_true.tolist() 
# 预测数据的标签 
date_pre = np.random.randint(0, 2, 5000) 
date_pre = date_pre.tolist() 
print("实际标签：", date_true) 
print("预测标签：", date_pre) 
TP = 0 
FP = 0 
TN = 0 
FN = 0 
# F1-score 函数


print("正例 F1-score 为：") 
print(f1(date_true, date_pre, 1)) 
print("反例 F1-score 为：") 
print(f1(date_true, date_pre, 0))