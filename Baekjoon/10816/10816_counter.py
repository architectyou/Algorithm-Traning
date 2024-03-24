import sys
from collections import Counter

sys.stdin = open("Baekjoon/test.txt", "r")

n = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))

# card_list의 각 요소별 등장 횟수를 계산
card_count = Counter(card_list)

m = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

# num_list의 각 요소가 card_count에 존재하는지 확인하고, 그 횟수를 checklist에 저장
checklist = [card_count[num] for num in num_list]

print(*checklist)
