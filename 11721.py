# 열 개씩 끊어 출력하기

n = input()
k = len(n)
for i in range(0, k, 10) :
    print(n[i:i + 10])