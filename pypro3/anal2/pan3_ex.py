# pandas 문제 1)
#   a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오. 
#      np.random.randn(9, 4)
#   b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No3, No4로 지정하시오
#   c) 각 컬럼의 평균을 구하시오. mean() 함수와 axis 속성 사용

import pandas as pd
import numpy as np
arr = pd.DataFrame(np.random.randn(9, 4) )
print(arr)
print()
arr.columns =['No1','No2','No3','No4']
print(arr)
print(arr.mean(axis = 0))
print(arr.mean())
print()
print('-----------------')
# pandas 문제 2)
# a)
df = pd.DataFrame(np.arange(10,41,10).reshape(4,1),index= ['a','b','c','d'])
df.columns=['numbers']
print(df)
print()

# b)
print(df.loc['c'])
print()

# c) 
print(df.loc['a'],df.loc['d'])
print()

# d)
print(df.sum())
print()

# e)
import math
# print(math.sqrt(list(df['numbers']))
print(df** 2)
print()

# f)
df['floats'] = [1.5, 2.5, 3.5, 4.5]
print(df)
print()

# g)
df['names'] = pd.Series(['길동', '오정', '팔계', '오공'],index= ['d', 'a', 'b', 'c'])
print('g)\n',df)






