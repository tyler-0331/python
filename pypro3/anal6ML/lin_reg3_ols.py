# ols 사용: 가장 기본적인 결정론적 선형회귀방법. 불확실정이 있다.

import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("../testdata/drinking_water.csv")
print(df.head(3))
print(df.corr())    # 피어슨 상관계수 !! 가 default 임

# 회귀분석 : 만족도와 적절성은 인과관계가 있다라는 가정하에  / 적절성이 독리변수 , 만족도는 종속변수
model = smf.ols(formula = '만족도 ~ 적절성', data = df).fit()
print(model.summary())

print('결정계수: ', model.rsquared)
print('p-value: ', model.pvalues)
print('예측값: ', model.predict()[:5])
print('실제값: ', df.만족도[:5].values)  # 가로로 데이터 뽑을때 !

# 시각화
import numpy as np
import matplotlib.pyplot as plt
plt.scatter(df.적절성, df.만족도)
slope , intercept = np.polyfit(df.적절성, df.만족도, 1)
plt.plot(df.적절성, df.적절성 * slope + intercept, 'b')
plt.show()














