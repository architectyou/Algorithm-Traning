#dp

import sys
sys.stdin = open("Baekjoon/test.txt", "r")

n = int(input())

## dp 풀이법 , [0]크기의 배열을 n+1개 만큼 만들기
dp = [0] * (n+1)

dp[1] = 1
dp[2] = 2

# 1*2 타일을 마지막에 놓는 경우, 2*(n-1) 크기의 직사갹형을 채우는 방법의 수와 같다.
# 2*1 타일을 마지막에 놓는 경우, 2*(n-2) 크기의 직사각형을 채우는 방법의 수와 같다.

# dp[n] = dp[n-1] + dp[n-2]

for i in range(3, n+1) :
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)