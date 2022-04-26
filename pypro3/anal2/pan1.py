# Pandas: 고수준의 자료 구조 (Serise, DataFrame)를 지원. 데이터분석용 자료 관리를 위한 다양한 함수 제공
# 축약 연산, sql처리, 시계열 데이터 처리, 시각화 ...

import pandas as pd
from pandas import Series
import numpy as np

# Series: 일련의 데이터를 담을 수 있는 1차원 배열과 비슷한 자료구조를 가지며, 색인을 지원함

obj = Series([3, 7, -5, 4])
# list, tuple type 가능. TypeError: 'set' type is unordered
print(obj, type(obj))

obj2 = Series([3, 7, -5, 4], index=['a', 'b', 'c', 'd'])
# 생성 시 색인을 지정 가능
print(obj2)
print(sum(obj2), obj2.sum(),np.sum(obj2))
print(obj2.values)    # [ 3  7 -5  4] 값만 가저 오기
print(obj2.index)   # Index(['a', 'b', 'c', 'd'], dtype='object')

print('---------------')
# 인덱싱, 슬라이싱
print(obj2) 
print(obj2[1])
print(obj2['b'])
print(obj2[['b']])
print(obj2[['a','b']])
print(obj2['a':'b'])

print('------------')
print(obj2[2])
print(obj2[1:4])
print(obj2[[2,1]])
print(obj2 > 1)
print('a' in obj2)

print('----------')
# dict type 으로 Series 객체 생성
names = {'mouse':5000, 'keyboard':25000, 'monitor':550000}
print(names)
obj3 = Series(names)
print(obj3)
obj3.index = ['마우스', '키보드','모니터']
print(obj3)
print(obj3['마우스'])
print()
obj3.name = '상품가격'
print(obj3)

print('\n~~~DataFrame~~~~~~~~~~~~~~~~~~~')
#DataFrame : 표 모양(2차원)의 자료구조로 여러 개의 칼럼(열)을 갖는다. 
from pandas import DataFrame
df = DataFrame(obj3)
print(df, type(df))   # <class 'pandas.core.frame.DataFrame'>

data = {
'irum':['홍길동', '한국인', '신기해', '공기밥', '한가해'],
'juso':('역삼동', '신당동', '역삼동', '역삼동', '신사동'),
'nai':[23, 25, 33, 30, 35],
}
print(data, type(data))

frame = DataFrame(data)
print(frame, type(frame))

print(frame['irum'],type(frame['irum']))
print(frame.irum)
print()
print(DataFrame(data, columns=['juso', 'irum','nai']))
print()
frame2 = DataFrame(data, columns = ['irum','nai','juso','tel'], index = ['a','b','c','d','e'])  # 결측치 tel
# frame2.columns = ['irum','nai','juso','tel']
# frame2.index = ['a','b','c','d','e']

print(frame2)

frame2['tel']="111-111"  # 모든 행에 적용
print(frame2)

val = Series(['222-2222','333-3333','444-4444'], index= ['b','c','e'])   # Series가 모여 dataFrame이 된다
print(val)
frame2['tel'] = val
print(frame2)
print('ttttttttttttttttt')
print(frame2.T)  # 전치  행과 열의 순서 바뀜!  transpose

print(frame2.values)  # 2차원 matrix , 중첩 리스트 
print(frame2.values[0,1])
print(frame2.values[0:2])

print()
frame3 = frame2.drop('d')  # 행 삭제 
# frame3 = frame2.drop('d', axis=0) # 행 삭제
# frame3 = frame2.drop('d', axis=1) # 열 삭제
print(frame3)

frame4 = frame2.drop('tel',axis=1) # 열 삭제  axis = 1 
print(frame4)
print()
print(frame2)
print(frame2.sort_index(axis=0, ascending=False)) # 행 단위 반대료 
print(frame2.sort_index(axis=0, ascending=True)) # 열 단위
print(frame2.rank(axis = 0))   # 콜럼별 순서 확인 

print()
print(frame2['juso'].value_counts())   # 건수 확인 할때 사용!! 

print()
data = {
    'juso':['강남구 역삼동','중구 신당동','강남구 대치동'],
    'inwon':[23,25,15],
}
fr = DataFrame(data)
print(fr)

result1 = Series([ju.split()[0]for ju in fr.juso])
print(result1.values)  # 리스트로 뽑아 보기
print(result1.value_counts())

result2 = Series([ju.split()[1]for ju in fr.juso])
print(result2)  

















