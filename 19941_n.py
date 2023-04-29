n, k = map(int, input().split())
bench = list(map(str, input()))
p_list = []
h_list = []

for i in range(0, n):
    if bench[i] == 'P':
        p_list.append(i)
    else :
        h_list.append(i)

def count_people(p, h):
    global p_list
    global h_list
    if abs(p - h) <= k :
        cnt = 1
        p_list.remove(p)
        h_list.remove(h)
    else :
        if p > h:
            h_list.remove(h)
        else :
            p_list.remove(p)
        cnt = 0
    return (cnt)

cnt = 0
while p_list and h_list :
    cnt += count_people(p_list[0], h_list[0])
print(cnt)