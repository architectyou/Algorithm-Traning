import sys
# sys.stdin = open("input.txt", "r")

# 두 리스트 합치기

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

res = n_list + m_list
res.sort(reverse = False)

print(*res)