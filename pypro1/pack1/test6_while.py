#반복문 : while 조건
a = 1

while a <= 5:
    print(a, end = ' ')
    a = a + 1
    
print('\nwhile 종료')

print()
i = 1
while i <= 3:
    j = 1
    while j <= 4:
        print('i:' + str(i) + ',j' + str(j))
        j += 1
    i += 1

print('\nwhile 종료2')

print('1~100 사이의 정수 중 3의 배수의 합')
i = 1; hap = 0
while i <= 100:
    #print(i, end = '')
    if i % 3 == 0:
        #print(i, end = ' ')
        hap += i
    i += 1
    
print('합은', hap)

print()
colors = ['r','g','b']
print(len(colors))
a=0
while a < len(colors):
    print(colors[a],end=':')
    a += 1
    
print()
while colors:
    print(colors.pop())

print(len(colors))

print()
i=1
while i <= 10:
    j = 1
    res = ''
    while j <= i:
        res = res + '*'
        j += 1
    print(res)
    i += 1

print()

# 문1) 1 ~ 100 사이의 숫자 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
'''
i=1 ; hap = 0
while i <=100:
    if (i % 3 == 0 | i % 2 == 0):
        print(i)
        i +=1
        hap += i
    print(hap) 
'''

i = 1; hap=0
while i <= 100:
    if i % 3 == 0 and i % 2 != 0:
        # print(i)
        hap += i        
    i += 1
print('합은', hap)  # 합은 867

# 문2) 2 ~ 5 까지의 구구단 출력
print()
a = 2
while a <= 5:
    j=1
    while j <= 9:
        print(a*j, end=' ')
        j+=1
    print()    
    a+=1   
'''   
i=1 ; j=2
while j <= 5:
    while i <=9:
        print(j*i, end =' ' )
        i +=1
    j+=1
'''    
         

# 문3) -1, 3, -5, 7, -9, 11 ~ 99 까지의 합을 출력
print()
b=1
ss = 0
while b < 100:
    if ss == 0:
        print(-b, end=' ')
        ss+=1
    else:
        print(b , end=' ')
        ss+=-1
    b+=2