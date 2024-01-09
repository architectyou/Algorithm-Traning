import sys
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

num = list(map(int,input().split()))
num.sort()

lt = 0
rt = n-1

# print(num)

while lt <= rt :
    mid = (lt+rt)//2

    if num[mid] == m :
            # index를 물어 본 게 아니라 몇 번 째 인지 물어봤으므로 mid + 1
            print(mid+1)
            break

    elif num[mid] > m :
        rt = mid -1

    elif num[mid] < m :
        lt = mid +1
