# 0 = not cute / 1 = cute

n = int(input())
no_cu = 0
cute = 0

for i in range(n) :
    a = int(input())
    if a == 0 :
        no_cu += 1
    elif a == 1 :
        cute += 1
if no_cu > cute :
    print("Junhee is not cute!")
else :
    print("Junhee is cute!")