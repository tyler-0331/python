# zz
'''
grades = [ 86,88,95,92]

def show_grades(grades):
    for i in grades:
        print(i, end=' ')
show_grades(grades)

def show_sum(grades):
    tot = 0
    for i in grades:
        tot += i
    return tot

print()
print('합은: ', show_sum(grades))

def show_avg(grades):
    tot = show_sum(grades)
    avg = tot/len(grades)
    return avg

print()
print('평균은: ' , show_avg(grades))
'''
'''
# numpy 2
print('---------------list.ndarray 기억상태 구분')
li = list(range(1,10))
print(li, '  ', len(li),'  ',type(li))
print(li[0],li[1])
print(id(li[0]), id(li[1]))   # 한 리스트에 있는 것들은 id가 다르다!!
print(li * 3)   # 1~9 까지의 수를 9번 반복해서 프린트한다
for i in li:
    print(i * 10, end=' ')    # 이게 모든 list에다 10을 곱한 것!!!

import numpy as np
print()
arr = np.array(li)
print(arr, type(arr))
print(id(arr[0]),id(arr[1]))   # numpy.ndarray는 id가 같다!!!
print(arr * 10)  

print('---'* 10)
a = np.array([1,2,3])   # 상위 타입을 따른다 
print(a, type(a), a.dtype, a.shape, a.ndim, a.size)
print(a[0],type(a[0]))
print(a[1:3], type(a[1:3]))
print(a[-1], type(a[-1]))
print()

b = np.array([[1,2,3],[4,5,6]])
print(b, type(b), b.dtype, b.shape, b.ndim, b.size)

c = np.zeros((2,2))
print(c)

d= np.ones((1,2))
print(d)

e= np.full((2,2),fill_value = 7)
print(e)

print(np.random.rand(5),np.mean(np.random.rand(5)))
print(np.random.randn(5),np.mean(np.random.randn(5)))

print()
np.random.seed(1)
print(np.random.randn(2,3))

print(np.random.randint(10, size=6))
print(np.random.randint(10, size=(5,5)))
print()
print(np.random.randint(10, size=(2,3,4)))

print()
print(list(range(1,10)),type(list(range(1,10))))
print(np.arange(10),type(np.arange(10)))

print()
print('-----인덱싱, 실라이싱 -----')
a = np.array([1,2,3,4,5])
print(a[1:5:2])  # 1 thorough 5 by 2 

print("ccccccc")
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a[:],type(a[:]))
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

print('-----------dddddd--')
a = np.array([[1,2,3],[4,5,6],(7,8,9)])   # list 나 tuple 로 array 안에 넣을수 있다.
print(a.shape)
r1 = a[1, :]
r2 = a[1:2, :]
print(r1,r1.shape)  # 1차원
print(r2,r2.shape)  # 2차원

print()
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])   
print(a.shape)
print(a)
b = np.array([0,2,0,1])   # a 배열 인덱싱용 배열 
print(b,b.shape)
print()
print(np.arange(4))
print(a[[1,2],[1,2]])
print(a[np.arange(4),b])

print()
bool_idx = (a > 10)
print(bool_idx)

print(a[bool_idx])  # ture인 것들만 나온다
print(a[a > 10]) 
'''

# numpy 3 
import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)  # data type은 따로 명시 가능!!
print(x, x.dtype)

y = np.arange(5,9).reshape(2,2)
y = y.astype(np.float64)
print(y,y.dtype)










