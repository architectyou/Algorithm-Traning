import sys
# sys.stdin = open("input.txt", "r")

# 카드 역배치 (정올 기출)

card = list(range(21))

for i in range(10):
    a, b = map(int, input().split())

    card[a:b+1] = card[b:a-1:-1]

del card[0]
print(*card)
