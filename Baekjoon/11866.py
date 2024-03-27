import sys
sys.stdin = open("Baekjoon/test.txt", "r")

from collections import deque

n, k = map(int, input().split())
que = deque()
result = []

for i in range(n):
    que.append(i+1)

while len(que) > 0 : 
    que.rotate(-1 * (k-1))
    result.append(que[0])
    que.popleft()

print("<" + str(result)[1:-1] + ">")