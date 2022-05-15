# [로지스틱 분류분석 문제2] 
# 게임, TV 시청 데이터로 안경 착용 유무를 분류하시오.
# 안경 : 값0(착용X), 값1(착용O)
# 예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv
# 새로운 데이터(키보드로 입력)로 분류 확인. 스케일링X

from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle 
import pandas as pd
import numpy as np

df = pd.read_csv('../testdata/bodycheck.csv')
print(df, type(df), len(df))

x = df[['게임','TV시청']]
y = df['안경유무']
print(df['안경유무'].unique()) #[0 1]
print(set(y))  # {0, 1}

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

logi_model = LogisticRegression(C= 0.01, random_state = 0)
logi_model.fit(x_train, y_train)

y_pred= logi_model.predict(x_test)
print('예측값 : ', y_pred)
print('실제값 : ', y_test.values)



