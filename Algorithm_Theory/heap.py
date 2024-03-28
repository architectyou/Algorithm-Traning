import sys
import heapq

input = sys.stdin.readline

# 파이썬에서 제공하는 heap 자료구조는 기본적으로 min heap 형태의 자료구조
# 따라서 오름차순 정렬이 수행된다.
# max heap 을 구현하고 싶다면 -를 붙여서 데이터를 넣거나 빼면 된다.

def heapsort(iterable) :
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable : 
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)) :
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n) :
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n) :
    print(res[i])