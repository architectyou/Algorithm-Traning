import sys
sys.stdin = open("test.txt", "r")

# n = int(input())

# dp = [float('inf')] * (n+1)
# dp[0] = 0

# # 동적 프로그래밍

# for i in range(3, n+1):
#     dp[i] = min(dp[i], dp[i-3] + 1)

# for i in range(5, n+1):
#     dp[i] = min(dp[i], dp[i-5] + 1)

# # 주어진 수를 최소로 나누기

# if dp[n] == float('inf') :
#     print(-1)
# else : 
#     print(dp[n])


# 동적 프로그래밍을 사용하지 않은 경우
    
n = int(input())
cnt = 0

while n >= 0 :
    if n % 5 == 0 :
        cnt += n//5
        print(cnt)
        break

    n -= 3
    cnt += 1

else :
    print(-1)