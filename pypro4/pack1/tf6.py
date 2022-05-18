import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation

# XOR 게이트 논리 모델을 생성 후 처리 
# 1. 데이터 셋 생성
x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,1,1,0])
print(x)  # feature
print(y)  # label(class)

# model = Sequential([
#     Dense(input_dim = 2, units= 1),
#     Activation('sigmoid')
# ])

# model = Sequential()
# model.add(Dense(units=5, input_dim = 2))
# model.add(Activation('relu'))
# model.add(Dense(units=1))
# model.add(Activation('sigmoid'))

model = Sequential()
model.add(Dense(units=5, input_dim = 2, activation = 'relu'))
model.add(Dense(units=5, activation = 'relu'))
model.add(Dense(units=5, activation = 'relu'))
model.add(Dense(units=1, activation = 'sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(x,y, epochs= 100, batch_size = 1, verbose= 0)   # batch_size를 늘려주면 속도가 빨라 진다. 몇변 학습하고 답을 맞추는 개념
loss_metrics = model.evaluate(x,y)
print('loss_metrics: ', loss_metrics)

pred = (model.predict(x) > 0.5).astype('int32')
# print('예측결과 : ', pred)
print('예측결과 : ', pred.flatten())   # 차원 축소 (2차원에서 1차원으로)

print('history: ', history.history)
print('loss: ', history.history['loss'])
print('accuracy: ', history.history['accuracy'])

# # 학습 진행 중 loss, accuracy를 시각화 
# import matplotlib.pyplot as plt 
# plt.plot(history.history['loss'], label = 'train loss') 
# plt.plot(history.history['accuracy'], label = 'train accuracy') 
# plt.xlabel('epochs')
# plt.legend(loc = 'best')
# plt.show()

print('-----------------')
print(model.layers)
print(model.summary())  # 모델에 대한 layer

print()
print(model.weights)









