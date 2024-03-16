import sys
sys.stdin = open("Baekjoon/test.txt", "r")

from collections import deque

n = int(input())

deq = deque(range(1, n+1))

if len(deq) == 1 :
    print(*deq)

else : 
    while len(deq) > 0 :
        deq.popleft()
        deq.rotate(-1)
        if len(deq) == 1: 
            print(*deq)
            break