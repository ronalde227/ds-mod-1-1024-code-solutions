# -*- coding: utf-8 -*-
"""Implementation_functions.ipynb

Automatically generated by Colab 1.
submission
Original file is located at
    https://colab.research.google.com/drive/1Tx1fQbZx37kKjtSCIXmTF4-tYGFzb-E0
"""

import pandas as pd
import numpy as np
import category_encoders as ce
import time

def load_data(df):
    df = pd.read_csv(df)
    return df

def clean_data(df):
    df = df.drop_duplicates()
    for i in df.columns:
      if(df[i].isnull().sum()>0):
        if df[i].dtypes in ['int64', 'float64'] and df[i].nunique()>100:
          df[i].fillna(df[i].mean(), inplace=True)
        elif df[i].dtypes in ['int64', 'float64'] and df[i].nunique()<=100:
          df[i].fillna(df[i].median(), inplace=True)
        elif df[i].dtypes == 'object':
          df[i] = df[i].fillna(np.random.choice(df[i].dropna().unique()))
    
    return df

def encode_data(df):
  category_list = []
  for col in df.select_dtypes(include = ['object']).columns:
    if(df[col].nunique() > 2 ):
      category_list.append(col)
  print(category_list)

  ce_target = ce.TargetEncoder(cols = category_list)
  ce_target.fit_transform(df[category_list],df['TARGET'])
  df[category_list] = ce_target.transform(df[category_list])

  return df, category_list, ce_target

def binary_encoder(df):
  for col in df.select_dtypes(include = ['object']).columns:
    if(df[col].nunique() == 2 ):
      first = df[col].unique()[0]
      second = df[col].unique()[1]
      df[col] = df[col].map({first:1,second:0})
    else:
      df[col] = 1
  return df

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import imblearn

def split_data(df):
  X = df.drop(['SK_ID_CURR', 'TARGET'], axis=1)
  y = df['TARGET']
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  #handling imbalance data
  rus = imblearn.under_sampling.RandomUnderSampler(random_state=42)
  X_train, y_train = rus.fit_resample(X_train, y_train)

  return X_train, X_test, y_train, y_test

import xgboost as xgb
from sklearn.metrics import roc_curve, roc_auc_score

def train_model(X_train, y_train):
  xgb_model = xgb.XGBClassifier(random_state=42)
  param_grid = {
    'max_depth': [10,50],
    'n_estimators': [50, 100],
    'learning_rate': [0.01, 0.1]
    }

  grid_search = GridSearchCV(xgb_model, param_grid=param_grid, cv=2, scoring='roc_auc', n_jobs=-1)

  start_time = time.time()
  grid_search.fit(X_train, y_train)
  end_time = time.time()

  print("Best Parameters:", grid_search.best_params_)
  print("Best Score:", grid_search.best_score_)
  xgb_model = grid_search.best_estimator_

  return xgb_model, start_time, end_time

