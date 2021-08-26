# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 17:48:09 2021

@author: LENOVO
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
#reading the data as the delimiter is different
data_set=pd.read_csv("winequality-red.csv",delimiter=';')
#data preprocessing steps
print("Rows and Columns: ",str(data_set.shape))
#print(duplicate_ds)
print(data_set.columns)

"""
fig = plt.figure() 
  
# creating the bar plot 
plt.bar([6,5,7,8,4,3,9],data_set['quality'].value_counts(),color ='red',width = 0.4) 
plt.xlabel("Quality Value") 
plt.ylabel("No. of instances") 
plt.title("Quality Instances") 
plt.show() 

#to check for any missing values
print("White wine quailty missing values: \n",data_set.isna().sum())

#reading the data as the delimiter is different
data_set=pd.read_csv("winequality-red.csv",delimiter=';')
#data preprocessing steps
print("Rows and Columns: ",str(data_set.shape))
#print(data_set.head())
#print(data_set.columns)
print(data_set['quality'].value_counts())
fig = plt.figure() 
  
# creating the bar plot 
plt.bar([5,6,7,4,8,3],data_set['quality'].value_counts(),color ='blue',width = 0.4) 
plt.xlabel("Quality Value") 
plt.ylabel("No. of instances") 
plt.title("Quality Instances") 
plt.show() 
"""
data_set_abb=data_set[["fixed acidity","volatile acidity","citric acid","quality"]]

corr=data_set_abb.corr()
plt.subplots(figsize=(10,10))
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cmap=sns.diverging_palette(220, 20, as_cmap=True))