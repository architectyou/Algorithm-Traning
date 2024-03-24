import sys
sys.stdin = open("Baekjoon/test.txt", "r")

### 시간초과
# n = int(sys.stdin.readline())
# card_list = list(map(int, sys.stdin.readline().split()))

# m = int(sys.stdin.readline())
# num_list = list(map(int, sys.stdin.readline().split()))

# checklist = [0] * m

# for i in range(m) :
#     for card in card_list : 
#         if num_list[i] == card :
#             checklist[i] += 1

import sys
n = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))

# cardlist의 각 요소별 등장요소 계산하기 - 딕셔너리 이용
card_count = {}
for card in card_list : 
    if card in card_count : 
        card_count[card] += 1
    else : 
        card_count[card] = 1

m = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

checklist = [card_count.get(num, 0) for num in num_list]

print(*checklist)