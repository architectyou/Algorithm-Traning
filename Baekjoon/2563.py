import sys
sys.stdin = open("Baekjoon/test.txt", "r")

# 색종이
input = sys.stdin.readline

# 도화지
paper = [[0 for _ in range(100)] for _ in range(100)]
# print(paper)

n = int(input())

cnt = 0 

for i in range(n):
    x, y = map(int, input().split())

    for x_idx in range(x, x+10) :
        for y_idx in range(y, y+10) :
            paper[x_idx][y_idx] = 1

for i in paper : 
    cnt += i.count(1)

print(cnt)