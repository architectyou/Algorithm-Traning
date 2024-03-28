import sys
sys.stdin = open("Baekjoon/test.txt", "r")

# 14425 문자열 집합

n, m = map(int, input().split())

# dict, set은 모두 해시테이블로 구성되어 있다.
# set은 value가 존재하지 않고 key만 존재하는 구조,
# dict 는 value-key 쌍으로 존재하는 구조

cnt = 0
answer = set(input() for _ in range(n))
result = []

for i in range(m) :
    word = input()

    if word in answer : 
        cnt += 1
    
    else : 
        continue

print(cnt)