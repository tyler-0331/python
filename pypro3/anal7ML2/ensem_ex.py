# kaggle.com이 제공하는 'Red Wine quality' 분류 ( 0 - 10)
# dataset은 winequality-red.csv 
# https://www.kaggle.com/sh6147782/winequalityred?select=winequality-red.csv

import pandas as pd

data = pd.read_csv('../testdata/winequality-red.csv')
print(data.head(3),data.shape)  # (1596, 12)
print(data.info())
data.drop(columns=['quality'],inplace= True)
print(data.isnull().sum())
print(data.head(3),data.shape)  #(1596, 11)






