# kaggle.com이 제공하는 'glass datasets'
# 유리 식별 데이터베이스로 여러 가지 특징들에 의해 7가지의 label(Type)로 분리된다.

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import xgboost as xgb
from xgboost import plot_importance
from lightgbm import LGBMClassifier
import matplotlib.pyplot as plt
from sklearn import metrics

df = pd.read_csv('../testdata/glass.csv')
print(df.head(3), df.shape) #(214, 10)
print(df.isnull().sum())
print(df.Type.unique())

from sklearn.preprocessing import LabelEncoder

df_x = df.drop(['Type'], axis=1) 
df_y = LabelEncoder().fit_transform(df['Type'])
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.2, random_state=12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (171, 9) (43, 9) (171,) (43,)

model = xgb.XGBClassifier(booster = 'gbtree', max_depth = 6, n_estimators= 500).fit(x_train, y_train)

print(model)
pred = model.predict(x_test)
print('예측값 :', pred[:10])
print('실제값 :', y_test[:10])
print('분류 정확도: ', metrics.accuracy_score(y_test, pred)) 
print('분류 보고서: ', metrics.classification_report(y_test, pred))

# 시각화
fig, ax = plt.subplots(figsize = (10, 12))
plot_importance(model, ax= ax)
plt.show()

