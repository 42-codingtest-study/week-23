n, k = map(int, input().split())
bench = list(map(str, input()))
h_list = []
p_list = []

for i in range(0, n):
    if bench[i] == 'H':
        h_list.append(i)
    elif bench[i] == 'P':
        p_list.append(i)
    else :
        print("Input Wrong")

# print("P: ", p_list)
# print("H: ", h_list)

def p_bigger_than_h(h, p):
    global p_list
    global h_list
    if (p - h) <= k :
        cnt = 1
        p_list.remove(p)
        h_list.remove(h)
    else :
        cnt = 0
        h_list.remove(h)
    return (cnt)

def h_bigger_than_p(h, p):
    global p_list
    global h_list
    if (h - p) <= k :
        cnt = 1
        p_list.remove(p)
        h_list.remove(h)
    else :
        cnt = 0
        p_list.remove(p)
    return (cnt)

cnt = 0
while p_list and h_list :
    p = p_list[0]
    h = h_list[0]
    # print("P: ", p, "H: ", h)
    if p > h :
        cnt += p_bigger_than_h(h, p)
    else :
        cnt += h_bigger_than_p(h, p)
    # print("cnt: ", cnt)

print(cnt)