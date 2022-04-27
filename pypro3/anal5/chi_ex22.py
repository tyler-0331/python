# 카이제곱 문제2) 지금껏 A회사의 직급과 연봉은 관련이 없다. 
# 그렇다면 정말로 jikwon_jik과 jikwon_pay 간의 관련성이 없는지 분석. 가설검정하시오.
#   예제파일 : MariaDB의 jikwon table 
#   jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
#   jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
#   조건 : NA가 있는 행은 제외한다.

# 귀무: A회사의 직급과 연봉은 관련이 없다. 독립적이다.
# 대립: A회사의 직급과 연봉은 관련이 있다. 종속적이다.

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

