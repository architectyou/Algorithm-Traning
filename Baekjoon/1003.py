import sys
sys.stdin = open("Baekjoon/test.txt", "r")

t = int(input())

for i in range(t) :
    n = int(input())
    dp = [0] * (n+2)

    if n == 0 : 
        dp[0] = 1
    elif n == 1 :
        dp[1] = 1

    while n >= 2 :
        dp[n-1] += 1 
        dp[n-2] += 1
        n -= 1
        if n == 1 : 
            break
    
    print(dp)
    print(dp[0], dp[1])


