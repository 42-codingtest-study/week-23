# 왜 하필 30인지 생각해봐라 이좌식아

n = list(map(int, input()))

def list_to_num(n_list):
    num = 0
    for i in n_list :
        num = num * 10 + i
    return (num)

num = 0

if 0 not in n:
    print(-1)
else :
    for i in n:
        num += i
    if num % 3 == 0 :
        n.sort(reverse=True)
        print(list_to_num((n)))
    else :
        print(-1)