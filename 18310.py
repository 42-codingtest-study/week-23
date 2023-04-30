n = int(input())
home = list(map(int, input().split()))
home = sorted(home)

print(home[(n-1)//2])
