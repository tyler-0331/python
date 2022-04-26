# example 
# 사번과 이름을 입력하여 로그인에 성공하면       buser,jikwon : join
# 사번, 직원명, 부서명, 부서전화, 연봉, 성별 출력
# 1, 홍길동, 영업부, 123-1234, 5000, 남

import MySQLdb

import pickle
with open('mydb.dat','rb') as obj:
    config = pickle.load(obj)

