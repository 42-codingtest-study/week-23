n, a, b, c, d = list(map(int, input().split()))
Amoney = 0
Bmoney = 0
count = 0
if n % a == 0:
    count = n // a
    Amoney = b * count
elif n % a != 0:
    count = n // a + 1
    Amoney = b * count
if n % c == 0:
    count = n // c
    Bmoney = d * count
elif n % c != 0:
    count = n // c + 1
    Bmoney = d * count

if Amoney >= Bmoney:
    print(Bmoney)
else:
    print(Amoney)
