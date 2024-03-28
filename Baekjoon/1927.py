import sys
sys.stdin = open("Baekjoon/test.txt", "r")

# 1927번 최소 힙
# 최소 힙은 이진 트리의 일종으로, 각 노드의 값이 해당 노드의 자식 노드 값보다 작거나 같은 이진 트리

import heapq


n = int(input())
arr = []

for i in range(n) :
    # print(arr)
    num = int(sys.stdin.readline().rstrip())
    if num > 0 :
        heapq.heappush(arr, num)
    elif num == 0 :
        if len(arr) == 0 : 
            print(0)
        else : 
            print(heapq.heappop(arr))