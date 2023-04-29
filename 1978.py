n = int(input())
num = list(map(int, input().split()))
num.sort()
cnt = 0

def is_prime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True

for i in range(n):
    if is_prime(num[i]):
        cnt += 1

print (cnt)