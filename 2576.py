# 홀수

res = []
for i in range(7):
    a = int(input())
    if a % 2 == 0:
        continue
    else:
        res.append(a)
        
if len(res) == 0:
    print(-1)
else:
    print(sum(res), min(res), sep="\n")