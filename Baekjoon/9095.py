import sys
sys.stdin = open("Baekjoon/test.txt", "r")

t = int(input())

for i in range(t) :
    n = int(input())
    
    dp = [0] * (n+1)

    for j in range(1, n+1) :
        if j == 1:
            dp[j] = 1
        elif j == 2 : 
            dp[j] = 2
        elif j == 3 :
            dp[j] = 4
        else : 
            dp[j] = dp[j-3] + dp[j-2] + dp[j-1]
    print(dp[j])


