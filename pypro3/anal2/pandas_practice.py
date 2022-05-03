import pandas as pd

names = {'mouse':5000, 'keyboard':25000, 'monitor':550000}
print(names, type(names))

obj = pd.Series(names)
print(obj)
obj.index = ['마우스', '키보드','모니터']
print(obj)
print(obj['마우스'])
obj.name = '상품가격'
print(obj)

print('\n~~~DataFrame~~~~~~~~~~~~~~~~~~~')
from pandas import DataFrame

df = pd.DataFrame(obj)
print(df)
data = {
'irum':['홍길동', '한국인', '신기해', '공기밥', '한가해'],
'juso':('역삼동', '신당동', '역삼동', '역삼동', '신사동'),
'nai':[23, 25, 33, 30, 35],
}

print(data, type(data))
df2 = pd.DataFrame(data)
print(df2)
print(df2['irum'],type(df2['irum']))
print()
print(df2.irum,type(df2.irum))
print()
print(DataFrame(data, columns=['juso', 'irum','nai']))




















