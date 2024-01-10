import sys
sys.stdin = open("input.txt", "r")

# 곶감 (모래시계)
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

s = 0
e = n
sum = 0

# 회전 정보
m = int(input())
for i in range(m):
    x, y, z = map(int, input().split())
    
    if y == 0 :
        for j in range(n):
            if j >= z :
                a[x][j] = a[x][j-z]
            else :
                a[x][j] = a[x][n-z]

    elif y == 1 :
        for j in range(n):
            if j >= z :
                a[x][j] = a[x][n-j+z]
            else :
                a[x][j] = a[x][n-j+z]

# 모래 시계
# for i in range(n):
#     for j in range(s, e):
#         sum += a[i][j]
#     if i < (n//2):
#         s += 1
#         e -= 1
#     else :
#         s -= 1
#         e += 1

for i in a:
    print(i)
