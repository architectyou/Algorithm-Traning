import sys
sys.stdin = open("Baekjoon/test.txt", "r")

t = int(input())

# 첫 번째 풀이코드 (정답 맞음)
# for _ in range(t) :
#     k = int(input())
#     n = int(input())

#     dp = [[0] * (n+1)] * (k+1) #index는 k 까지

#     for i in range(1, n+1) :
#         dp[0][i] = i

#     for i in range(1, k+1) :
#         dp[i][1] = 1
#         for j in range(1, n+1) :
#             if i == 0 : 
#                 dp[i][j] = j
#             if (i>=1) & (j >=2) : 
#                 dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            
#     # print(dp)
#     print(dp[k][n])

for _ in range(t):
    k = int(input())
    n = int(input())

    dp = [[0] * (n+1) for _ in range(k+1)]  # 각각 독립된 리스트 생성

    for i in range(1, n+1):
        dp[0][i] = i  # 0층 i호에는 i명이 삽니다.

    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]  # 문제의 규칙에 맞게 업데이트

    print(dp)
    print(dp[k][n])