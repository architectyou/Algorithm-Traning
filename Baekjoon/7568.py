import sys
sys.stdin = open("Baekjoon/test.txt", "r")

input = sys.stdin.readline

n = int(input())
big = []

for i in range(n):
    x, y = map(int, input().split())
    big.append((x, y))

for i in range(n):
    rank = 1
    for j in range(n):
        if i != j: 
            # 현재 나와 나머지 사람들을 모두 비교
            if big[i][0] < big[j][0] and big[i][1] < big[j][1]:
                rank += 1
    print(rank, end=" ")