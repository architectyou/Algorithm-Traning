## 숫자 카드

import sys
sys.stdin = open("Baekjoon/test.txt", "r")


n = int(input())
n_list = sorted(list(map(int, input().split())))

m = int(input())
m_list = (list(map(int, input().split())))


def binary_serach(arr, value) :
    lt = 0
    rt = len(arr) - 1

    while lt <= rt : 
        mid = (lt + rt) // 2
        if arr[mid] == value : 
            return print(1, end = " ")
        elif arr[mid] < value :
            lt = mid + 1
        else : 
            rt = mid - 1

    return print(0, end = " ")

## python 에서 in list 이용시 평균적으로 시간복잡도 O(n)
# 딕셔너리와 set은 내부적으로 해시테이블을 만들기 때문에 평균적으로 O(1)의 시간복잡도로 확인할 수 있음.

# n_list가 크고 m_list 크기가 작으며, n_list가 이미 정렬되어 있는 경우, 이진 탐색 방식이 더 효율적일 수 있음.
# 반면 m의 크기가 매우 크고 n이 상대적으로 작은 경우 딕셔너리를 사용하는 방식이 더 나을 수 있음.
for i in m_list :
    binary_serach(n_list, i)
