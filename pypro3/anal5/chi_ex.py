# 카이제곱 검정
# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
#   예제파일 : cleanDescriptive.csv
#   칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
#   조건 :  level, pass에 대해 NA가 있는 행은 제외한다.
import pandas as pd
import scipy.stats as stats

data = pd.read_csv('../testdata/cleanDescriptive.csv').dropna(subset = ['level','pass'])
pd.set_option('display.max_columns',500)
print(data.head(3))


# 귀무: 부모학력 수준이 자녀의 진학여부와 관련이 없다
# 대립: 부모학력 수준이 자녀의 진학여부와 관련이 있다

ctab = pd.crosstab(index = data['level'], columns = data['pass'])
ctab.index=['고졸','대졸','대학원졸']
ctab.columns=['합격','불합격']
print(ctab)

chi2, p, df, _ = stats.chi2_contingency(observed=ctab)
print(chi2,p)
print(df)

# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
# 예제파일 : cleanDescriptive.csv
# 칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
# 조건 :  level, pass에 대해 NA가 있는 행은 제외한다.
import pandas as pd
import scipy.stats as stats

data = pd.read_csv("../testdata/cleanDescriptive.csv")
df = pd.DataFrame(data)
print(df)
data = df.dropna(subset=['level', 'pass'], how='any')
print(data.head(5))
print(data['level'].unique())
print(data['pass'].unique())
ctab = pd.crosstab(index =data['level'], columns=data['pass'])
ctab.index = ['고졸','대졸','대학원졸']
ctab.columns = ['합격','실패']
print(ctab)
chi_result = [ctab.loc['대학원졸'],ctab.loc['대졸'],ctab.loc['고졸']]
chi2, p, ddof, _ = stats.chi2_contingency(ctab)

print('chi2:{}, p:{}, ddof:{}'.format(chi2,p,ddof))
#해석 : 유의

# 카이제곱 문제2) 지금껏 A회사의 직급과 연봉은 관련이 없다. 
# 그렇다면 정말로 jikwon_jik과 jikwon_pay 간의 관련성이 없는지 분석. 가설검정하시오.
#   예제파일 : MariaDB의 jikwon table 
#   jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
#   jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
#   조건 : NA가 있는 행은 제외한다.
'''
import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from conda.common._logic import TRUE
plt.rc('font',family='malgun gothic')
import csv

try:
    with open('mydb.dat', mode = 'rb') as obj:
        config = pickle.load(obj)
        
except Exception as e:
    print('연결 오류 : ',e)

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_jik,jikwon_pay
        from jikwon 
    """
    df = pd.read_sql(sql,conn)
    print(df)

except Exception as e:
    print('연결 오류 : ',e)
finally:
    cursor.close()
    conn.close()
'''



