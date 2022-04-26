# 1) step1 : array 관련 문제
'''
정규분포를 따르는 난수를 이용하여 5행 4열 구조의 다차원 배열 객체를 생성하고, 각 행 단위로 합계, 최댓값을 구하시오.
< 출력 결과 예시>
1행 합계   : 0.8621332497162859
1행 최댓값 : 0.3422690004932227
2행 합계   : -1.5039264306910727
2행 최댓값 : 0.44626169669315
3행 합계   : 2.2852559938172514
3행 최댓값 : 1.5507574553572447
'''
import numpy as np
np.random.seed(1)
x = np.random.randn(5,4)
print(x)
print()
i = 1
for n in x:
    print(i,'행 합계: ',np.sum(n))
    print(i,'행 최댓값: ',np.max(n))
    i += 1

print()
print()
# 2) step2 : indexing 관련문제
'''
 문2-1) 6행 6열의 다차원 zero 행렬 객체를 생성한 후 다음과 같이 indexing 하시오.
   조건1> 36개의 셀에 1~36까지 정수 채우기
   조건2> 2번째 행 전체 원소 출력하기 
              출력 결과 : [ 7.   8.   9.  10.  11.  12.]
   조건3> 5번째 열 전체 원소 출력하기
              출력결과 : [ 5. 11. 17. 23. 29. 35.]
   조건4> 15~29 까지 아래 처럼 출력하기
              출력결과 : 
              [[15.  16.  17.]
              [21.  22.  23]
              [27.  28.  29.]]
'''
arr = np.zeros((6,6))
print(arr)
print()
#  조건 1 
num = 0
for i in range(6):
    for j in range(6):
        num += 1
        arr[i,j] = num 
print(arr)

print()
# 조건 2 
print(arr[[1]])  # 2차원
print(arr[1])    # 1차원
print(arr[1,:])  # 1차원
print(arr[1:2])
print()

# 조건 3
print(arr[:,4])
print()

# 조건 4
print(arr[2:5,2:5])
print()
#  문2-2) 6행 4열의 다차원 zero 행렬 객체를 생성한 후 아래와 같이 처리하시오.
#      조건1> 20~100 사이의 난수 정수를 6개 발생시켜 각 행의 시작열에 난수 정수를 저장하고, 두 번째 열부터는 1씩 증가시켜 원소 저장하기
#      조건2> 첫 번째 행에 1000, 마지막 행에 6000으로 요소값 수정하기
# <<출력 예시>>
# 1. zero 다차원 배열 객체
#   [[ 0.  0.  0.  0.]
#         ...
#    [ 0.  0.  0.  0.]]

arr = np.zeros((6,4))
print(arr)
r = np.random.randint(20,100,6)
print(r)
print()

r = list(r)
print(r)

for i in range(len(arr)):
    num = r.pop(0)
    for j in range(len(arr[0])):
        arr[i,j] = num
        num += 1
print(arr)

# 4. 첫 번째 행에 1000, 마지막 행에 6000으로 수정
#  [[ 1000.  1000.  1000.  1000.]
#   [   40.    41.    42.    43.]
#   [  100.   101.   102.   103.]
#   [   22.    23.    24.    25.]
#   [   52.    53.    54.    55.]
#   [ 6000.  6000.  6000.  6000.]]

arr[0,:] = 1000
arr[-1,:] = 6000
print(arr)


# 3) step3 : unifunc 관련문제
print()
#  표준정규분포를 따르는 난수를 이용하여 4행 5열 구조의 다차원 배열을 생성한 후
#  아래와 같이 넘파이 내장함수(유니버설 함수)를 이용하여 기술통계량을 구하시오.
#  배열 요소의 누적합을 출력하시오.

arr = np.random.randn(4,5)
print(arr)
print()

print('평균 :', np.mean(arr))
print('합계: ', arr.sum())
print('표준편차: ', arr.std())
print('분산: ', np.var(arr) )
print('최댓값: ',arr.max())
print('최소값: ',arr.min())
print('1사분위 수 :' , np.percentile(arr,25))
print('2사분위 수 :' , np.percentile(arr,50))
print('3사분위 수 :' , np.percentile(arr,75))
print('요소값 누접합: ', np.cumsum(arr))





