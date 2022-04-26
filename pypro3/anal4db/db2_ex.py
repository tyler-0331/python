# pandas 문제 5)
#  MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.
#      - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
#      - DataFrame의 자료를 파일로 저장
#      - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
#      - 부서명, 직급으로 교차테이블을 작성(crosstab)
#      - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
#      - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성

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
        select jikwon_no,jikwon_name,buser_name,jikwon_pay,jikwon_jik
        from jikwon inner join buser
        on buser_num = buser_no
    """
    sql2 = """
        select * 
        from jikwon left outer join gogek
        on jikwon_no = gogek_damsano
    """
    sql3 = """
        select * from jikwon
    """
    cursor.execute(sql)
    
    df = pd.read_sql(sql,conn)
    df.columns = ['사번','이름','부서명','연봉','직급']
    print(df)
    print()
    
    """
    with open('jik_data2.csv',mode = 'w', encoding = 'UTF-8') as fobj:
        writer = csv.writer(fobj)
        for r in cursor:
            writer.writerow(r)
    """
    
    print('부서명별 인원수 : ',df['부서명'].value_counts())
    print('부서명별 연봉의 합 : ',df.pivot_table(['연봉'], index = ['부서명'], aggfunc = np.sum))
    print('부서명별 연봉의 최대값 : ', df.groupby(['부서명'])['연봉'].max())
    print('부서명별 연봉의 최소값 : ', df.groupby(['부서명'])['연봉'].min())
    
    ctab = pd.crosstab(df['부서명'], df['직급'], margins = True)  # 건수 확인 (crosstab)
    print(ctab)
    
    print()
    df2 = pd.read_sql(sql2, conn)
    print(df2)
    
   
    
except Exception as e:
    print('연결 오류 : ',e)
finally:
    cursor.close()
    conn.close()



