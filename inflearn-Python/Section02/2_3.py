# # k 번째 큰 수

import sys
sys.stdin = open("input.txt", "rt")

n , k = map(int, input().split())

card = list(map(int, input().split()))

result = set()

#하나씩 제거하면서 뽑기
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            # print(card[i])
            # print(card[j])
            # print(card[m])
            result.add(card[i]+card[j]+card[m])

result = list(result)
result.sort(reverse=True)
print(result[k-1])
            
            


# # 중복 되는 값 제하기 (set) 이용하기
## solution

# import sys
# sys.stdin = open("input.txt", "rt")

# n, k = map(int, input().split())
# a = list(map(int,input().split()))
# res = set()

# # 3중 for 문 이용하기

# for i in range(n):
#     for j in range(i+1, n):
#         for m in range(j+1, n):
#             res.add(a[i]+a[j]+a[m])
            
# # set은 sort가 안됨

# res = list(res)
# res.sort(reverse=True)
# print(res[k-1])