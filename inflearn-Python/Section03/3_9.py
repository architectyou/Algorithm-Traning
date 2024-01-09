import sys
sys.stdin = open("input.txt", "r")

# 좌표판에서 움직이는 것 처럼 확인하기 위함
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())

# 격자
# a = list(list(map(int, input().split())) for _ in range(n))
# 같은 내용
a = [list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0]*n)
a.append([0]*n)

for x in a :
    x.insert(0, 0)
    x.append(0)
    print(x)

cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        # python all -> 모든 조건이 참일때만 참이 되는 함수
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(len(dx))) :
            cnt += 1

print(cnt)