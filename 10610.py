# 30

num = list(input())
num.sort(reverse = True)
k = ''

for i in num :
    k += i

if int(k) % 30 == 0 :
    print(k)
    
else :
    print(-1)