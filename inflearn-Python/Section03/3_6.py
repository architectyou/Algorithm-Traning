import sys
sys.stdin = open("input.txt", "r")

# 격자판 최대합

n = int(input())

# 2차원 리스트 -> 배열?
# for문을 돌리면서 n바퀴 해서 list n개 만들기
a = [list(map(int, input().split())) for _ in range(n)]

# for x in a :
#     print(x)

# 최댓값 구하기
largest = -214700000

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        # 행의 합 구하기
        sum1 += a[i][j]
        # 열의 합 구하기
        sum2 += a[j][i]
    if sum1 > largest :
        largest = sum1
    if sum2 > largest :
        largest = sum2

# 대각선의 합 구하기
sum1 = sum2 = 0

for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]

if sum1 > largest : 
    largest = sum1

if sum2 > largest :
    largest = sum2

print(largest)

