str = list(map(str, input()))
cnt = 0

for i in range (0, len(str)) :
    if i != 0 and i != len(str) - 1 :
        if str[i] == ' ' :
            cnt += 1
cnt += 1

if len(str) == 1 :
    if str[i] == ' ':
        cnt = 0
    else :
        cnt = 1

print(cnt)