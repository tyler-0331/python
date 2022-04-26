# 원격  DB(MariaDB)와 연동 처리 : DataFrame
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
        select jikwon_no,jikwon_name,buser_name,jikwon_jik,jikwon_gen,jikwon_pay
        from jikwon inner join buser
        on buser_num = buser_no
       """
    cursor.execute(sql)
    
    # 출력1 : console
    for (a,b,c,d,e,f) in cursor:
        print(a,b,c,d,e,f)
    
    # 출력 2 : DataFrame
    df1 = pd.DataFrame(cursor.fetchall(), columns = ['jikwon_no','jikwon_name','buser_name','jikwon_jik','jikwon_gen','jikwon_pay'])
    print(df1.head(3))
    
    print()
    # 출력 3 : csv file로 저장
    """ 
    with open('jik_data.csv',mode = 'w', encoding = 'UTF-8') as fobj:
        writer = csv.writer(fobj)
        for r in cursor:
            writer.writerow(r)
    """
    df2 = pd.read_csv("jik_data.csv", header = None, names = ['번호', '이름', '부서', '직급', '성별', '연봉'])
    print(df2.head(3))
    
    print()
    df = pd.read_sql(sql, conn)
    df.columns = ['번호', '이름', '부서', '직급', '성별', '연봉']
    print(df.head(3))
    # DataFrame에 저장된 자료로 기술통계, 추론통계
    print()
    print(df[:3])
    print('건수 : ', len(df))
    print('건수 : ',df['이름'].count())
    print()
    print('직급별 인원수 : ',df['직급'].value_counts())
    print('부서별 인원수 : ',df['부서'].value_counts()) 
    print('연봉 평균 : ',df.loc[:, '연봉'].mean())
    print('연봉 표준편차 : ',df.loc[:,'연봉'].std())
    print()
    print(df.loc[:,'연봉'].describe())
    print(df.loc[df['연봉'] >= 8000])
    print()
    ctab = pd.crosstab(df['성별'], df['직급'], margins = True)
    print(ctab) # 성별, 직급별 건수 확인
    
    print()
    print(df.groupby(['성별','직급'])['이름'].count())
    print(df.pivot_table(['연봉'], index = ['성별', '직급'], aggfunc = np.mean))
    
    # 시각화 pie
    jik_ypay = df.groupby(['직급'])['연봉'].mean()
    print(jik_ypay, type(jik_ypay))
    print(jik_ypay.index)
    print(jik_ypay.values)
    
    plt.pie(x = jik_ypay, explode = (0.2,0,0,0.3,0), labels = jik_ypay.index,
            shadow = True, labeldistance = 0.7, counterclock = False)
    plt.show()

except Exception as e:
    print('연결 오류 : ',e)
finally:
    cursor.close()
    conn.close()
    