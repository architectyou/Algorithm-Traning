import sys
sys.stdin = open("Baekjoon/test.txt", "r")

# 포켓몬
n,m = map(int, input().split())

# 해시테이블 이용해서 풀기

poketmon = {}
num = {}

for i in range(1, n+1) :
    name = sys.stdin.readline().rstrip()
    poketmon[i] = name
    num[name] = i

for j in range(m) :
    answer = sys.stdin.readline().rstrip()
    if answer.isdigit() :
        print(poketmon.get(int(answer)))
    else : 
        print(num.get(answer))