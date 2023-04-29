arr = [int(input()) for _ in range(9)]
print (max(arr))

print (arr.index(max(arr)) + 1)
# 와우 저렇게 짧아지다니
# for i in range (9):
#     if arr[i] == max(arr):
#         print(i + 1)
#         exit()