# 상관관계 문제)
# https://github.com/pykwon/python 에 있는 Advertising.csv 파일을 읽어 tv,radio,newspaper 간의 상관관계를 파악하시오. 
# 그리고 이들의 관계를 heatmap 그래프로 표현하시오. 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("../testdata/Advertising.csv")
print(data)

print(data.corr())
print(data.corr(method='pearson'))

import seaborn as sns
sns.heatmap(data.corr())
plt.show()






