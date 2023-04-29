n = int(input())
home = list(map(int, input().split()))
home.sort()

if n % 2 != 0:
    print(home[n // 2])
else :
    mid1 = home[n // 2 - 1]
    mid2 = home[n // 2]
    sum1, sum2 = 0, 0
    for i in home:
        sum1 += abs(mid1 - i)
        sum2 += abs(mid2 - i)
    if sum1 <= sum2:
        print(home[n // 2 - 1])
    else :
        print(home[n // 2])