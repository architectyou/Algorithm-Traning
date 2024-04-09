import sys
sys.stdin = open("Baekjoon/test.txt", "r")


from collections import deque

n, m = map(int, input().split())
que = deque(i for i in range(1, n+1))

num_list = list(map(int, input().split()))

def pop() :
    que.popleft()
    return que

def rotate_r() :
    que.rotate(1)
    return que

def rotate_l() :
    que.rotate(-1)
    return que

# rotate 연산이 최소가 되도록 로직을 구성해야 함.
cnt = 0 

for num in num_list : 
    while que[0] != num : 
        idx = que.index(num)
        if idx <= len(que) // 2 :
            rotate_l()
            cnt += 1
        else : 
            rotate_r()
            cnt += 1
    pop()

print(cnt)