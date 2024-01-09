import sys
sys.stdin = open("input.txt", "r")

# 수들의 합

n, m = map(int, input().split())

num_list = list(map(int, input().split()))

sum = 0
cnt = 0

for i in range(n):

    sum += num_list[i]

    if num_list[i] == m: 
        cnt += 1 
        sum = 0

    elif sum == m :
        cnt += 1
        sum = num_list[i]

print(cnt)
