import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

sum_list = []

for i in range(n):
    for j in range(m):
        sum = (i+1) + (j+1)
        sum_list.append(sum)

res = {}

for i in sum_list:
    try : res[i] += 1
    except : res[i] = 1

sorted_dict = sorted(res.items(), key = lambda x : x[1], reverse = True)

arrMin = float('-inf')
result = []

# 딕셔너리 내 원소 비교
for i in range(len(sorted_dict)):
    if (sorted_dict[i][1]) > arrMin:
        arrMin = sorted_dict[i][1]
        
        for j in range(len(sorted_dict)):
            if sorted_dict[j][1] == arrMin:
                print(sorted_dict[j][0], end = " ")




### solution

n, m = map(int, input().split())

# 정다면체 주사위의 눈의 합 n+m
cnt = [0]*(n+m+3)
max = 0

for i in range(1, n+1) :
    for j in range(1, m+1):
        cnt[i+j] += 1
        
#cnt list에서 최댓값 찾기

for i in range(n+m+1) :
    if cnt[i]>max : 
        max = cnt[i]
        
for i in range(n+m+1):
    if cnt[i] == max : 
        print(i, end = " ")