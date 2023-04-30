n, k = map(int, input().split())
where = list(input())
count = 0

for i in range(n):
    if where[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0 <= j < n:
                if where[j] == 'H':
                    where[j] = '0'
                # print("where: ", j, where)
                    count += 1
                    break
print(count)
