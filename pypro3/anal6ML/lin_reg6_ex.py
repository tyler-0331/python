# 회귀분석 문제 3) 
# kaggle.com에서 Carseats.csv 파일을 다운 받아 Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.
# 변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.
# 회귀분석모형의 적절성을 위한 조건도 체크하시오.
# 완성된 모델로 Sales를 예측.

import  statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font',family='malgun gothic')

df = pd.read_csv("../testdata/Carseats.csv")
print(df)
print(df.columns)
print(df.describe())
print(df.US)
# print('상관계수(r): ', df.loc[:,['Sales','CompPrice']].corr())
# print('상관계수(r): ', df.loc[:,['Sales','Income']].corr())
# print('상관계수(r): ', df.loc[:,['Sales','Advertising']].corr())  # 0.269507
# print('상관계수(r): ', df.loc[:,['Sales','Population']].corr())
# print('상관계수(r): ', df.loc[:,['Sales','Price']].corr())    # -0.444951
# print('상관계수(r): ', df.loc[:,['Sales','ShelveLoc']].corr())
# print('상관계수(r): ', df.loc[:,['Sales','Age']].corr())   # -0.231815
# print('상관계수(r): ', df.loc[:,['Sales','Education']].corr())

model1 = smf.ols(formula = 'Sales ~ Income+ Advertising + Price + Age', data= df).fit()
print(model1.summary())
print('설명력: ', model1.rsquared)  # 0.35954932981031396
print('p-value: ', model1.pvalues[1])  # 1.355422296117433e-28

# 예측
df.Income = int(input("인컴을 입력하세요: "))
df.Advertising = int(input("광고 횟수를 입력하세요: "))
df.Price = int(input("가격을 입력하세요: "))
df.Age = int(input("나이를 입력하세요: "))

new_data = pd.DataFrame({'Income':df.Income,'Advertising':df.Advertising ,'Price':df.Price ,'Age':df.Age })
pred_new = model1.predict(new_data)
print('입력값 예측 Sales 값: ', pred_new)





