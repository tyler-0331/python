# 로지스틱 회귀분석 (Logistic linear regression)
# 날씨 데이터로 비유무 예측 분류 모델

import  pandas as pd
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np

data = pd.read_csv("../testdata/weather.csv")
print(data.head(3), data.shape)  # (366, 12)
data2 = pd.DataFrame()
data2 = data.drop(['Date', 'RainToday'], axis= 1)
data2['RainTomorrow'] = data2['RainTomorrow'].map({'Yes':1, 'No':0})
print(data2.head())
print(data2['RainTomorrow'].unique())

print()
# train(모델학습) / test(모델평가) 분리: 과적합 방지 
train, test = train_test_split(data2, test_size = 0.3, random_state = 42)
print(train[:3], train.shape)  # (256, 10)
print(test[:3], test.shape)    # (110, 10)

# model 
# formula = 'RainTomorrow ~ ' 
col_select = "+".join(train.columns.difference(['RainTomorrow']))
print(col_select)
formula = 'RainTomorrow ~ ' + col_select
# model = smf.glm(formula = formula, data = train, family = sm.families.Binomial()).fit()
model = smf.logit(formula = formula, data = train).fit()   # logit 으로 할때만 confusion matrix 를 볼수 있다. 
print(model.summary())

print('예측값: ', np.rint(model.predict(test)[:5].values))
print('실제값: ', test['RainTomorrow'][:5].values)

conf_mat = model.pred_table()    # AttributeError: 'GLMResults' object has no attribute 'pred_table'
print(conf_mat)

from sklearn.metrics import accuracy_score
pred = model.predict(test)
print('분류 정확도: ', accuracy_score(test['RainTomorrow'],np.rint(pred)))   # 0.872727



