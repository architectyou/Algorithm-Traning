import sys
sys.stdin = open("Baekjoon/test.txt", "r")

from collections import deque

n, k = map(int, input().split())

deq = deque()
result = []

for i in range(n) :
    deq.append(i+1)

while len(deq) > 0 :
    deq.rotate(-1 * (k-1))
    result.append(deq[0])
    deq.popleft()

result_str = "<" + str(result)[1:-1] + ">"
print(result_str)