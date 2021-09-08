# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 10:57:07 2021

@author: Seong
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('eda_data.csv')

# Choose relevant columns
df.columns

df_model = df[['average_salary', 'Rating', 'Size', 'Type of ownership', 
             'Sector', 'Industry', 'Revenue', 
             'hourly', 'employer_provided', 'job_state', 'python', 
             'job_sim', 'seniority', 'desc_len']]

# get dummy data
df_dum = pd.get_dummies(df_model)

# train test split to generalize models
from sklearn.model_selection import train_test_split

X = df_dum.drop('average_salary', axis = 1)
y = df_dum.average_salary.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# multiple linear regression
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)

cross_val_score(lm, X_train,y_train, scoring='neg_mean_absolute_error')
# lasso regression
# random forest
# tune models w/ GridsearchCV
# test ensembles