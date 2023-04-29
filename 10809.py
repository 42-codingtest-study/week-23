from string import ascii_lowercase

alpha = dict()
for i in ascii_lowercase:
    alpha[i] = -1

str = list(map(str, input()))
for i in range (len(str)- 1, -1, -1) :
    alpha[str[i]] = i

for key, value in alpha.items() :
    print(value, end=' ')