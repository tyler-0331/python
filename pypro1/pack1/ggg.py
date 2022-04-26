i = list(range(1,101))
hap = 0
check = 0
for a in i:
    if a % 2 == 1:
        check += 1
        hap += a
        
print('합은 :',hap,'갯수 :', check) 