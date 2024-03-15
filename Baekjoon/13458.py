import sys
sys.stdin = open("Baekjoon/test.txt", "r")

# 각 시험장마다 필요한 감독관의 최소 수 출력하기

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

res = 0

for i in range(n):

    if a[i] >= b : 
        main = a[i] - b
        sub  = main % c
        if sub == 0 : 
            res += (main//c) +1 
        else : 
            res += (main//c) + 2
    else : 
        res += 1

print(res)
