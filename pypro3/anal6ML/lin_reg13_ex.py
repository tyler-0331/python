# 회귀분석 문제 5) 
# Kaggle 지원 Consumo_cerveja.csv dataset으로 회귀분석 모델(LinearRegression)을 작성하시오.
# Beer Consumption - Sao Paulo : 브라질 상파울루 지역 대학생 그룹파티에서 맥주 소모량 dataset
# feature : Temperatura Media (C) : 평균 기온(C)
#             Precipitacao (mm) : 강수(mm)
# label : Consumo de cerveja (litros) - 맥주 소비량(리터) 를 예측하시오
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, r2_score 

df = pd.read_csv("../testdata/Consumo_cerveja.csv",
                 usecols=['Temperatura Minima (C)','Precipitacao (mm)','Consumo de cerveja (litros)']
                 )
df.dropna(inplace=True)
df.columns = ['기온','강수','소비량']
df['기온']= df['기온'].apply(lambda x:x.replace(',','.'))
df['강수']= df['강수'].apply(lambda x:x.replace(',','.'))

print(df.head(3))
df.info()
print(df.shape) # (365, 3)
print(df.corr(method='pearson'))

x = df[['기온','강수']]
y = df[['소비량']]

model = LinearRegression().fit(x, y)
pred = model.predict(x)
print('예측값 : ', np.round(pred[:5].T))
print('실제값 : ', np.round(y[:5].T))

print('RMSE : ', mean_squared_error(y, pred))
print('r2_score : ', r2_score(y, pred))

new_params = [[30,10]]
new_pred = model.predict(new_params)
print('기온이 %s, 강수량이 %s 경우에 맥주 소비량은 약 %s'%(new_params[0][0],new_params[0][1], new_pred[0]))