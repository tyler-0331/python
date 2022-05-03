# 회귀분석 문제 2) 
# testdata에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
# 이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.  수학점수를 종속변수로 하자.
#   - 국어 점수를 입력하면 수학 점수 예측
#   - 국어, 영어 점수를 입력하면 수학 점수 예측
import statsmodels.api
import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font',family = 'malgun gothic')


data = pd.read_csv("../testdata/student.csv")
print(data.corr())

#   - 국어 점수를 입력하면 수학 점수 예측
model1 = smf.ols(formula = '수학 ~ 국어',data = data).fit()
print(model1.summary())  # 8.16e-05 < 0.05 

data.국어 = int(input("국어 점수를 입력하세요: "))
pred_math1 = model1.predict(pd.DataFrame({'국어':data.국어}))
print(pred_math1[0])


#   - 국어, 영어 점수를 입력하면 수학 점수 예측
model2 = smf.ols(formula = '수학 ~ 국어 + 영어', data = data).fit()
data.국어 = int(input("국어 점수를 입력하세요: "))
data.영어 = int(input("영어 점수를 입력하세요: "))

pred_math2 = model2.predict(pd.DataFrame({'국어':data.국어, '영어':data.영어}))
print(pred_math2[0])