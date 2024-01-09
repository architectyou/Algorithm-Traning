import sys
sys.stdin = open("input.txt", "rt")

n , k = map(int, input().split())

n_div = []

for i in range(n):
    if n % (i+1) == 0:
        n_div.append(i+1)
        
n_div.sort()
# k번째로 작은 약수 출력
if k <= len(n_div):
    print(n_div[k-1])
else : 
    print(-1)
