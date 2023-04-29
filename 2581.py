# 입력변수
m = int(input())
n = int(input())
# 필요함수
def is_prime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True
# 필요변수
ans = 0
flag = 0
# 찾는단계
for i in range(m, n + 1):
    if is_prime(i) :
        ans += i
        if flag == 0 :
            flag = i
# 출력부
if ans != 0 :
    print (ans, flag, sep="\n")
else :
    print(-1)
