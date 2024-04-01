import sys
sys.stdin = open("Baekjoon/test.txt", "r")

n = int(input())

# 각 집의 앞 뒤로 다른 색이 칠해져야 함.

# greedy 접근법 : 첫 번째 집에서 가장 비용이 적은 색을 선택하고, 이후의 집들에 대해
# 이전 집과 다른 색 중에서 가장 비용이 적은 색을 선택하는 방식 -> local minimum으로 최솟값을 보장하지 못함.

# dp 접근법 : dp 테이블을 정의해서 0부터 i번째 집까지 칠하는 데 드는 최소 비용으로 정의하기
# 점화식 : i번째 집을 각 색으로 칠했을 때 최소 비용은 i-1번째 집을 다른 두 색으로 칠했을 때의 비용 중 
# 최소 값에 현재 집을 해당 색으로 칠했을 때의 비용을 더한 값

# 집마다 다른 색을 칠할 때의 비용
cost = [list(map(int, input().split())) for _ in range(n)]
# 아래 for문 만드는 법 
# for i in range(n) :
#     house = list(map(int, input().split()))

dp = [[0] * 3 for _ in range(n)]

# 초기값 설정
dp[0] = cost[0]

# 최소 비용 계산
# 이전까지 구한 다른 색상의 컬러 + 현재 집의 컬러 색상을 더했을 때 최솟값이 되는 경우를 찾으면 됨.
for i in range(1, n) :
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[-1][0], dp[-1][1], dp[-1][2]))

# # 다른 풀이

dp = [[0] * 3 for _ in range(n+1)]

for i in range(n) :
    for j in range(3) :
        temp = float('inf')
        for k in range(3) :
            if j == k :
                # 이전에 칠한 게 아닌 경우에만 temp에 값을 저장해서 출력
                # 그게 빨간색이든, 초록색이든, 파란색이든 -> 모든 cost 값을 더한다
                continue
            temp = min(temp, cost[i][j] + dp[i][k])
        dp[i+1][j] = temp

print(dp[n])
print(min(dp[n]))