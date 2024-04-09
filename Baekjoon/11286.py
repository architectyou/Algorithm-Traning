import sys
sys.stdin = open("Baekjoon/test.txt", "r")
import heapq
#  절댓값 힙

input = sys.stdin.readline
n = int(input().rstrip())

heap = []

for i in range(n) :
    x = int(input().rstrip())
    if x != 0 : 
        #(원본값, 절댓값)
        heapq.heappush(heap, (abs(x), x))
    else : 
        if len(heap) == 0 :
            print(0)
        else : 
            value = heapq.heappop(heap)
            print(value[1])
# print(heap)