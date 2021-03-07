# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:26:29 2021

@author: HUAWEI
"""
#用python实现F1-score，并创建一个简单数据集进行测试
import numpy as np
 
y_true =  np.random.randint(0, 2, 5000) 
y_pred =  np.random.randint(0, 2, 5000) 
 
#true positive
TP = np.sum(np.logical_and(np.equal(y_true,1),np.equal(y_pred,1)))
print('TP :',TP)
 
#false positive
FP = np.sum(np.logical_and(np.equal(y_true,0),np.equal(y_pred,1)))
print('FP :',FP)
 
#true negative
TN = np.sum(np.logical_and(np.equal(y_true,1),np.equal(y_pred,0)))
print('TN :',TN)
 
#false negative
FN = np.sum(np.logical_and(np.equal(y_true,0),np.equal(y_pred,0)))
print('FN :',FN)

P = TP/(TP+FP)  
R = TP/(TP+FN)
print("正例 F1-score 为：",P)
print("反例 F1-score 为：",R)
