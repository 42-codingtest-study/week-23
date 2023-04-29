a = int(input())
b = int(input())
c = int(input())
num = a * b * c
num_list = []

while num != 0 :
    num_list.append(num % 10)
    num //= 10

for i in range (0, 10):
	cnt = 0
	for j in range (0, len(num_list)) :
		if num_list[j] == i :
			cnt += 1
	print(cnt)
