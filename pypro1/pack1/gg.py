print('---11번---')
i = 3

while i <= 9:
    j=1
    if i % 2 == 1:
        while j <= 9:
            print(i,'*', j, '=', i*j, end=' ')
            j += 1
        print()
    i += 1 
print()
print('---12번---')
hap = 0
for i in range(1,100):
    if i % 5 == 0:
        print(i)
        hap += i 
print(hap)


def func():
    hap = 0
    for i in range(1,100):
        if i % 5 == 0:
            hap += i 
    return hap

func()

print()
print('---13번---')
i = list(range(1,101))
hap = 0
check = 0
for a in i:
    if a % 2 == 1:
        check += 1
        print(a, end = ' ')
        hap += a
        
print('합은 :',hap,'갯수 :', check) 
        
print()    
print('---14번---')    
i = 1; hap = 0; check = 0
while i <= 100:
    if i % 2 == 0:
        check += 1
        hap += i
    i += 1
    
print(hap, check)        

print()
print('---15번---')       
for i in range(1,3):
    for j in range(1,3):
        if (i + j) % 2 == 0:
            print('첫번째 동전:'+str(i)+' 두번째 동전:'+str(j))

        
        
        
        
        
        
        
        