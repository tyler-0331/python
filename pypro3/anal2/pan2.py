from pandas import Series, DataFrame

data = Series([1,3,2],index = (1,4,2))
print(data)

data2 = data.reindex((1,2,4))  # re-indexing,  행 순서 재배치 
print(data2)

print()
data3 = data.reindex([0,1,2,3,4,5])   # 대응 값이 없는 인덱스는 Nan(결측값)으로 대치
print(data3)
print()
print(data2.reindex([0,1,2,3,4,5],fill_value = 777))  # 대응 값이 없는 인덱스는 777로 채워짐   
print()
print(data2.reindex([0,1,2,3,4,5],method ='ffill'))  # Nan 앞 값으로 현재 NaN을 대체
print(data2.reindex([0,1,2,3,4,5],method ='pad'))
print()
print(data2.reindex([0,1,2,3,4,5],method ='bfill'))  # Nan 뒷 값으로 현재 NaN을 대체
print(data2.reindex([0,1,2,3,4,5],method ='backfill'))

print('--------------------')
import numpy as np
df = DataFrame(np.arange(12).reshape(4,3), index = ['1월','2월','3월','4월'],  columns =['강남','강북','서초'])
print(df)
print(df['강남'])
print(df['강남'] > 3)
print(df[df['강남'] > 3])
print()
df[df < 3]= 0  # 3보다 작은 값을 다 0 으로 바꾸기 (조건치환)
print(df)

print('슬라이싱 관련 메소드 : loc()--- 라벨 지원, iloc() 숫자 지원 ----')
print(df['강남'])
# 복수 인섹싱 
print(df.loc['3월'])  #3월 행
print(df.loc['3월',])
print(df.loc['3월',:])
print()
print(df.loc[:'3월']) #3월 행 이하 모든 열 출력
print(df.loc[:'3월',['서초']])

print()
print(df.iloc[2])  # 2행 출력
print(df.iloc[2, :])  # 2행 출력
print(df.iloc[:3])  # 3 미만 행 출력
print(df.iloc[:3 , 2])  # 3 미만 행, 2열 출력
print(df.iloc[1:3,1:3])  

print('---------연산-----------')
s1 = Series([1,2,3], index = ['a','b','c'])
s2 = Series([4,5,6,7], index = ['a','b','d','c'])
print(s1)
print(s2)
print(s1 + s2)  # 인덱스 명 끼리 연산     - , *, /
print(s1.add(s2))  # 인덱스 명 끼리 연산  sub, mul, div 

print()
df1 = DataFrame(np.arange(9).reshape(3,3),columns=list('kbs'), index =['서울','대전','부산'])
df2 = DataFrame(np.arange(12).reshape(4,3),columns=list('kbs'), index =['서울','대전','제주','광주'])
print(df1)
print(df2)
print()
print(df1 + df2)
print(df1.add(df2,fill_value = 0))   # add를 쓸때 fill 쓸수 있다.!!  #NaN은 0 으로 채움  sub, mul, div




















