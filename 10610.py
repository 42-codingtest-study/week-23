n = list(input())
n = sorted(n, reverse=True)
sum = 0
for i in range(len(n)):
    sum += int(n[i])
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    # n.sort()
    print(''.join(n))
# print(sum)
