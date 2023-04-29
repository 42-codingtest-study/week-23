# 입력변수
n, m = map(int, input().split())
card = list(map(int, input().split()))
# 필요변수
ans = 0
card.sort()
# 갱신단계
for i in range(0, n - 2) :
    for j in range(i + 1, n - 1) :
        for k in range(j + 1, n):
            hat = card[i] + card[j] + card[k]
            if ans < hat and hat <= m :
                ans = hat
# 출력부
print (ans)