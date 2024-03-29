import sys
sys.stdin = open("Baekjoon/test.txt", "r")

#호출되는 동적테이블 만들기
dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41) :
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

## 조건에 따라 테이블에서 값 찾기
t = int(sys.stdin.readline().rstrip())

for i in range(t) :
    n = int(sys.stdin.readline())

    print(dp[n][0], dp[n][1])