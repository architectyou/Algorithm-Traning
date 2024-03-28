import sys
sys.stdin = open("Baekjoon/test.txt", "r")

# 최대 힙 계산하기

import heapq

n = int(sys.stdin.readline().rstrip())

arr = []

for i in range(n) :
    num = int(sys.stdin.readline().rstrip())
    print(arr)
    if num > 0 : 
        heapq.heappush(arr, -num)
        # append 를 사용할 경우, 단순히 arr 끝에 -num의 요소를 추가하기 때문에 O(1) 의 시간 복잡도를 가지지만
        # 추가된 요소가 리스트의 힙의 속성(최소 힙 혹은 최대힙)을 유지하지 않는다.
        # 따라서 나중에 호출하더라도 올바른 최솟값 혹은 최댓값을 보장하지 못한다.
        # arr.append(-num)
    elif num == 0 :
        if len(arr) == 0 :
            print(0)
        else : 
            res = -heapq.heappop(arr)
            print(res)