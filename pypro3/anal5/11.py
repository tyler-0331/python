# 다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다.
# 포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 two-sample t-검정을 하시오.
'''
import numpy as np
import scipy.stats as stats

blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]

# 귀무: 포장지 색상에 따른 제품의 매출액에 차이가 없다.
# 대립: 포장지 색상에 따른 제품의 매출액에 차이가 있다.

print(np.mean(blue))  # 72.8
print(np.mean(red))   # 63.8

two_sample = stats.ttest_ind(blue, red)
print(two_sample)
# Ttest_indResult(statistic=2.9280203225212174, pvalue=0.008316545714784403)
# pvalue=0.008316 < 0.05 이므로 귀무가설 기각!
# 포장지 색상에 따른 제품의 매출액에 차이가 있다.
'''

# 남아 신생아 몸무게의 평균 검정을 수행하려고 한다.
# 파일명 : babyboom.csv (testdata 폴더에 있음) # 1:여아, 2:남아 

# 남아 신생아의 몸무게는 평균이 3000(g)으로 알려져 왔으나 이것이 틀렸다는 주장이 나왔다.
# 표본으로 남아를 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정하시오.

# 귀무 : 남아 신생아의 몸무게는 평균이 3000(g) 이다.
# 대립 : 남아 신생아의 몸무게는 평균이 3000(g)이 아니다.
"""
import numpy as np
import scipy.stats as stats
import pandas as pd

data = pd.read_csv('../testdata/babyboom.csv')
print(data.head(3),len(data)) # 44
print(data.isnull().sum()) # 결측치 0 개
bdata = data[data['gender'] == 2]
print(bdata.head(3), len(bdata))  # 남아의 수는 26
print(np.mean(bdata.weight))  # 3375.30

print(stats.shapiro(bdata.weight)) # pvalue=0.2022 정규성 만족 

print(stats.ttest_1samp(bdata.weight, popmean= 3000))
# Ttest_1sampResult(statistic=4.47078356044109, pvalue=0.00014690296107439875)
# pvalue=0.0001469 < 0.05 이므로 귀무가설 기각
"""

# 에이콘 주식회사에서 영업사원들의 '지각횟수'와 '판매횟수' 간에 관계가 있는지 알아보려고 한다.
# 영업사원 5명을 대상으로 한 달 동안 '지각횟수'와 '판매횟수'를 조사했더니 아래와 같은 결과를 얻었다.
# 둘 사이의 상관계수를 출력하고 상관관계가 있는지 설명하시오.
"""
import pandas as pd
import numpy as np

# 지각횟수(x) = 1,2,3,4,5
# 판매횟수(y) = 8,7,6,4,5

df = pd.DataFrame({'late':(1,2,3,4,5),'sale':(8,7,6,4,5)})
print(df.corr(method='pearson'))
print(np.corrcoef(df.late, df.sale))
"""

# 소득 수준에 따른 외식 성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다.
# 'eat_out.txt' 데이터에 대하여 소득 수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시한다.
# ① 소스 코드와 모델의 분류정확도를 출력하시오.
# ② 키보드로 소득 수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하시오.

# 조건1 : 모델 생성은 glm 함수를 사용하도록 한다.
# 조건2 : 키보드로 입력할 소득 수준 값은 45로 한다.

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
from sklearn.metrics import accuracy_score

data = pd.read_csv('../testdata/last_test.csv')
print(data)
eatout = data[(data.요일 == '토')| (data.요일 == '일')]
print(eatout)

formula = '외식유무 ~ 소득수준'
result = smf.glm(formula = formula, data = eatout, family = sm.families.Binomial()).fit()  # binomial 을 넣기 때문에 이항분포가 된다
print(result)
print(result.summary())

pred = result.predict(eatout)
print('정확도: ', accuracy_score(eatout['외식유무'], np.around(pred)))

key = int(input('소득 수준 입력 : 45를 눌러주세요...'))
newdf = pd.DataFrame({'소득수준':[key]})
pred2 = result.predict(newdf)
print(np.rint(pred2.values))
