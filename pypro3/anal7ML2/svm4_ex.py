# Heart 데이터는 흉부외과 환자 303명을 관찰한 데이터다. 
# 각 환자의 나이, 성별, 검진 정보 컬럼 13개와 마지막 AHD 칼럼에 각 환자들이 심장병이 있는지 여부가 기록되어 있다. 
# dataset에 대해 학습을 위한 train과 test로 구분하고 분류 모델을 만들어, 모델 객체를 호출할 경우 정확한 확률을 확인하시오. 
# 임의의 값을 넣어 분류 결과를 확인하시오.

from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('../testdata/Heart.csv')
print(df.head(3))
print(df.info())
print(df.Ca.head(3))
print(df.isnull().sum())

df.Ca = df.Ca.fillna(df.Ca.mean())
print(df.isnull().sum())

# 더미화 
# dfy = dfy.map({'No':0, 'Yes':1})
# print(dfy[:3])

x_feature = df.drop(['Unnamed: 0','AHD','ChestPain','Thal'],axis = 1)
# print(x_feature)
y_label = df['AHD']

# 더미화 
# y_label = y_label.map({'No':0, 'Yes':1})
# print(y_label[:3])

data_train, data_test, label_train, label_test = train_test_split(x_feature, y_label, test_size = 0.3,random_state = 1)
print(data_train.shape, data_test.shape, label_train.shape, label_test.shape) # (212, 12) (91, 12) (212,) (91,)

model = svm.LinearSVC(C = 100).fit(data_train, label_train)
model2 = svm.SVC(C = 1).fit(data_train, label_train)


pred = model.predict(data_test)
pred2 = model2.predict(data_test)

print('실제값 : ', label_test[:10].values)
print('예측값 : ', pred[:10])    # LinearSVC
print('예측값2 : ', pred2[:10])   # SCV

print(metrics.accuracy_score(label_test, pred))  # LinearSVC
print(metrics.classification_report(label_test, pred))

print(metrics.accuracy_score(label_test, pred2))  # SCV













