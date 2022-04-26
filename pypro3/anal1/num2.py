# numpy 기본 이해

import numpy as np

print(np.__version__)

s = 'tom'

ss = ['tom', 'james','oscar']
print(ss,type(ss))
ss2 = np.array(ss)
print(ss,type(ss2))  # <class 'numpy.ndarray'>

print('---------------list.ndarray 기억상태 구분')
li = list(range(1,10))
print(li)
print(id(li[0]),id(li[1]))
print(li * 10)
print('-' * 10)

for i in li:
    print(i * 10, end = ' ')

print()
print([i*10 for i in li])   # 유연성이 좋다  type의 상관없이 list 에 다 때려넣을수 있다. 그래서 속도가 다소느림

print()  # list to ndarry 
num_arr = np.array(li)      # 유연성이 떨어 지나 속도가 빠르다!! 
print(num_arr)
print(id(num_arr[0]),id(num_arr[1]))
print(num_arr * 10)

print()
# a = np.array([1,2,3.2,'2'])   # 타입이 일치해야 한다!! numpy 의 array는  # 데이터는 상위 타입을 따름  int -> float -> complx -> str
a = np.array([1,2,3]) 
print(a, type(a), a.dtype, a.shape, a.ndim, a.size)
print(a[0])     # 인덱싱
print(a[1:3])   # 슬라이싱
print(a[-1])    # 뒤에서 첫 번째 

print()
b = np.array([[1,2,3],[4,5,6]])
print(b, type(b), b.dtype, b.shape, b.ndim, b.size)
print(b[0])     # 인덱싱
print(b[1:],)   # 슬라이싱
print(b[-1],)    # 뒤에서 첫 번째 
print(b[0,0],b[1,1])
print(b[[0]])

print('---------------')
c= np.zeros((2,2))
print(c)

d= np.ones((1,2))
print(d)

e= np.full((2,2),fill_value = 7)
print(e)

f= np.eye(3)    # 단위행렬 생성
print(f)

print()
print(np.random.rand(5),np.mean(np.random.rand(5)))   # 균등분포
print(np.random.randn(5),np.mean(np.random.rand(5)))  # 정규분포

np.random.seed(1)
print(np.random.randn(2,3))

print(np.random.randint(10,size=6))       # 1차원
print(np.random.randint(10,size=(3,4)))   # 2차원
print(np.random.randint(10,size=(3,4,5))) # 3차원

print()
print(list(range(0,10))) # list
print(np.arange(10))     # array

print('-----인덱싱, 실라이싱 -----')
a = np.array([1,2,3,4,5])
print(a[1:5:2])

print("ccccccc")
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a[:])
print(a[1:])
print(a[-1:])
print(a[0],a[0][0],a[0,0], a[[0]])   # 반환값이 : 1 차원, 스칼라, 2차원
print(a[1:,0:2])

print()
b = a[:2,1:3]   #서브 배열
print(b)
print(b[0,0])
print(a[0,1])
print()
b[0,0] = 88  # 서브 배열을 바꿔 주면 원래 배열에도 영향을 미친다!!! 
print(b)
print()
print(a)

print()
c = a[:2,1:3].copy()   # 배열 사본 복사   
print(c)
c[0,0] = 99            # .copy 를 쓰고 배열을 수정하면 원본에는 영향을 미치지 않는다. 배열을 따로 하나 생성 !! 
print(c)
print()
print(a)

print('-----------dddddd--')
a = np.array([[1,2,3],[4,5,6],(7,8,9)])   # list 나 tuple 로 array 안에 넣을수 있다.
print(a.shape)
r1 = a[1, :]
r2 = a[1:2, :]
print(r1,r1.shape)  # 1차원
print(r2,r2.shape)  # 2차원

print('----------------')
print()
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])   
print(a.shape)
print(a)
b = np.array([0,2,0,1])   # a 배열 인덱싱용 배열 
print(b,b.shape)
print()
print(np.arange(4))
print(a[np.arange(4),b])

print()
bool_idx = (a > 10)
print(bool_idx)

print(a[bool_idx])  # ture인 것들만 나온다
print(a[a > 10])

















