import sys
sys.stdin = open("Baekjoon/test.txt", "r")

t = int(input())

for i in range(t) :
    # 출발점, 도착점
    x1, y1, x2, y2 = map(int, input().split())

    n = int(input())
    cnt = 0

    for j in range(n) :
        c_x, c_y, r = map(int, input().split())
        # 원을 지나가야 하는 경우 하나씩 추가하기
        # 원의 방정식 (x-a)^2 + (y-b)^2 = r^2
        sp = ((x1 - c_x)**2 + (y1 - c_y)**2) <= (r**2)
        ep = ((x2 - c_x)**2 + (y2 - c_y)**2) <= (r**2)

        if sp == ep  :
            continue
        else : 
            cnt += 1
        # print(sp, ep)

    print(cnt)