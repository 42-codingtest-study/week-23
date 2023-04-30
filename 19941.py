# 햄버거

n, k = map(int, input().split())
place = list(input())
cnt = 0

for i in range(n):
    if place[i] == 'P':
        for j in range(max(i - k, 0), min(i + k + 1, n)):
            if place[j] == 'H':
                place[j] = 0
                cnt += 1
                break
print(cnt)