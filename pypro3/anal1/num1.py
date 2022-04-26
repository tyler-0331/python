# numpy : 고속연산, ndarry를 지원
# 데이터 분석 관련 모듈 전체 생태계의 핵심을 이루고 있기에 잘 다룰줄 알아야 한다.

# 평균, 분산, 표준편차 구하기 (모집단/ 통계량)
# grades = [1, 3, -2, 4]    # 변량(변수, 확률값, 관측값)  # 편차 제곱의 평균 = variance 그리고 루트를 씌운 값이 표준편차 
grades = [1, 2, 3, 4]
 
def show_grades(grades):
    for g in grades:
        print(g, end= ' ')

show_grades(grades)

def grades_sum(grades):
    tot=0
    for g in grades:
        tot += g
    return tot

print()
print('합은: ', grades_sum(grades))

def grades_avg(grades):
    tot = grades_sum(grades)
    ave = tot/ len(grades)
    return ave

print('평균은 :', grades_avg(grades))

def grades_variance(grades):
    ave = grades_avg(grades)
    vari = 0 
    for su in grades:
        vari += (su - ave)** 2
    return vari / len(grades)   # 모집단으로 계산(python)
    # return vari / (len(grades) -1)  # 표본집단으로 계산 (R)
    
print('분산은 :', grades_variance(grades))

import math
def grades_std(grades):
    # return grades_variance(grades) ** 0.5  # ** 0.5 는 루트 씌우기로 사용 가능! 
    return math.sqrt(grades_variance(grades))

print('표준편차는 :', grades_std(grades))

print()
print('numpy로 계산')
import numpy as np
#print('합은', numpy.sum(grades))
print('합은:', np.sum(grades))
print('평균은:', np.average(grades))
print('평균은:', np.mean(grades))
print('분산은:', np.var(grades))
print('표준편차는:', np.std(grades))











