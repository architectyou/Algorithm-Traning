import sys
sys.stdin = open("Baekjoon/test.txt", "r")

from collections import deque

# 1. 현재 queue의 가장 앞에 있는 문서의 중요도를 확인한다.
# 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
# 이 문서를 인쇄하지 않고 queue의 가장 뒤에 재배치한다. 

t = int(sys.stdin.readline())

for i in range(t) : 
    n, m = map(int, sys.stdin.readline().split())
    que = deque(map(int, sys.stdin.readline().split()))
    # i, idx에 대한 값을 튜플로 저장함.
    que = deque([(i, idx) for idx, i in enumerate(que)])

    cnt = 0

    while True : 
        # que의 첫번째 숫자가 max인 숫자와 같다면
        if que[0][0] == max(que, key=lambda x : x[0])[0] : 
            # 하나씩 더해감
            cnt += 1
            if que[0][1] == m : 
                # 첫 번째 숫자의 인덱스가 입력으로 받은 m 과 일치한다면
                # 그 때 카운트 값을 바로 출력 
                print(cnt)
                break
            else : 
                # 일치하지 않는다면 제외
                que.popleft()
        else : 
            # 첫 번째 숫자가 최댓값이 아니라면 뒤로 보낸다.
            que.append(que.popleft())