# 배열 연산 

import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)  # data type은 따로 명시 가능!!
print(x, x.dtype)
y = np.arange(5,9).reshape(2,2)   # 5~ 8  # 2행 2열    reshape 으로 구조 바꾸기
y = y.astype(np.float64)
print(y,y.dtype)

print()
print(x + y)
print(np.add(x,y))

print()
print(x - y)
print(np.subtract(x,y))

print()
print(x * y)
print(np.multiply(x,y))

print()
print(x / y)
print(np.divide(x,y))

print()
v = np.array([9,10])
w = np.array([11,12])
print(v * w)  # [99 120]
print()
print(v.dot(w))  # 219 벡터 내적 연산   v[0] * w[0] + v[1] * w[1]  
print(np.dot(v,w)) # 결과가 스칼라로 나온다 차원 축소 

print(x.dot(v)) # x[0,0] *v[0] + x[0,1] * v[1]     x[1,0] *v[0] + x[1,1] * v[1] 
print(np.dot(x,v))

print(x.dot(y))     # 2차원은 2차원 return
print(np.dot(x,y))

print()
print(x)
print(np.sum(x))
print(np.sum(x,axis = 0)) # 열에 대한 합 
print(np.sum(x,axis = 1)) # 행에 대한 합 
print(np.argmax(x),np.argmin(x))   # 가장 큰값이 있는 위치 # 최대 값은 인덱스 리턴!!!

print()
print(x)
print(x.T)            # 전치 !! 행과 열을 바꿔준다  
print(x.transpose())
print(x.swapaxes(0,1))

print('--------------')
# Broadcasting 연산: 크기가 다른 배열간 연산을 하면 작은 배열이 큰 배열의 크기에 자동으로 맞춰져 연산
x = np.arange(1,10).reshape(3,3)
print(x)
y = np.array([1,2,3])
print(x+y)

# file io
print()
datas = np.arange(0,10,2)
print(datas)
np.save('test1',datas)    # binary 형식으로 저장
np.savetxt('test2.txt',datas)    # 저장 할때는 savetxt
 
mydatas = np.loadtxt('test2.txt')  # 불러 올때는 loadtxt
print(mydatas)



 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 