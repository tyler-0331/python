# 에러 발생에 따른 예외 처리
# logic error, exception error : 파일, 네트워크, db, 키보드 ... 

def divide(a, b):
    return a/b

print('뭔가를 하다가 ...')
# c= divide(5,2)
# c= divide(5,0) # ZeroDivisionError: division by zero
# print(c)

try:
    c= divide(5,2)
    # c= divide(5,0)
    print(c)
    
    aa= [1,2]
    #print(aa[2])
    print(aa[1])
    
    open('c:/adb.txt')
    
except ZeroDivisionError:
    print('두번째 숫자는 0 ... shit..')   # 내가 원하는 대로 error 메세지 띄우기
except IndexError as er:
    print('참조 범위 오루: ',er)     # 원래 주는 error 프리트도 포함 시키고 싶을떄 
except Exception as e:        # 모든 에러 한번에 다 처리 !!!!
    print('에러처리: ', e)
finally:
    print('에러와 상관없이 반드시 수행')

print('종료')





