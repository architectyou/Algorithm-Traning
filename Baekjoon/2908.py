import sys
sys.stdin = open("Baekjoon/test.txt", "r")

a, b = sys.stdin.readline().split()

from collections import deque

a_que = deque(a)
b_que = deque(b)

def swap_num(que) :
    result = 0
    for i in range(3) :
        result += (int(que.pop()) * 10 ** (2-i))
    return print(result)

if a_que[-1] > b_que[-1] :
    swap_num(a_que)
elif a_que[-1] == b_que[-1] :
    if a_que[-2] > b_que[-2] :
        swap_num(a_que)
    elif a_que[-2] == b_que[-2] :
        if a_que[-3] > b_que[-3] :
            swap_num(a_que)
        else : 
            swap_num(b_que)
    else : 
        swap_num(b_que)
else : 
    swap_num(b_que)

# 더 간결한 코드
# a, b = sys.stdin.readline().split()

# a_rev = int(a[::-1])
# b_rev = int(b[::-1])

# print(max(a_rev, b_rev))
# ...