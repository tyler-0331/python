# 최소제곱해를 선형 행렬 방적식으로 얻기 

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.5, 2.1])

# plt.plot(x, y, 'o', label='Original data', markersize=10)
# plt.grid()
# plt.show()

A = np.vstack([x, np.ones(len(x))]).T
print(A)   # 4 * 2 

import numpy.linalg
w, b = np.linalg.lstsq(A, y)[0]  # 최소자승법 (내부적으로 편미분 사용)
print('w:', w, ',b: ',b )
# 단순선형회귀식 : y = 0.959999 * x +  -0.989999
print('예측값: ' , 0.959999 * 0 +  -0.989999)
print('예측값: ' , 0.959999 * 1 +  -0.989999)
print('예측값: ' , 0.959999 * 2 +  -0.989999)
print('예측값: ' , 0.959999 * 3 +  -0.989999)
print('미지의 예측값: ' , 0.959999 * 10 +  -0.989999)

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, w*x + b, 'r', label='Fitted line')
plt.grid()
plt.legend()
plt.show()



























