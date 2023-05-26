n, m, k = list(map(int, input().split()))
m2 = n - m
k2 = n - k

print(min(m,k) + min(m2, k2))

