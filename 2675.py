t = int(input())

for _ in range(t):
    r, s = map(str, input().split())
    for i in s:
        print(i * int(r), end='')
    print()

# 문자열 리스트말고 써보자
# for _ in range(t):
#     r, s = map(str, input().split())
#     for i in range (len(s)):
#         for _ in range (int(r)):
#             print(s[i], end='')
#     print()
