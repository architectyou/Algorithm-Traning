import sys
sys.stdin = open("Baekjoon/test.txt", "r")

## 듣보잡 
# n = 듣도 못한 사람 수 
# m = 보도 못한 사람 수
# 듣도 보도 못한 사람 -> 출력 (사전순으로)

n, m = map(int, input().split())
non_listen = set()
non_seen = set()
cnt = 0 

## in 함수는 set 함수를 사용하게 될 때 해시테이블을 이용하므로 O(1)의 시간복잡도를 갖는다.
for i in range(n) : 
    non_listen.add(sys.stdin.readline().rstrip())

for i in range(m) :
    non_seen.add(sys.stdin.readline().rstrip())

result = sorted(list(non_listen & non_seen))

print(len(result))
for i in result : 
    print(i)