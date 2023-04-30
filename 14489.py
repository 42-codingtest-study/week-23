a, b = map(int, input().split())
c = int(input())
price = 2*c
money = a + b

if money - price >= 0:
    print(money - price)
else :
    print(money)
