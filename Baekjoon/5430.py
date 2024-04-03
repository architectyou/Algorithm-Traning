import sys
sys.stdin = open("Baekjoon/test.txt", "r")

from collections import deque
# 생각보다 시간 복잡도를 많이 차지함.
# 출력시 띄어쓰기 때문에 리스트를 그대로 출력하면 안됨...
import ast

t = int(input())

for i in range(t) :
    function = list(sys.stdin.readline().rstrip())

    n = int(sys.stdin.readline().rstrip())
    num_list = deque(ast.literal_eval(sys.stdin.readline().rstrip()))

    reverse = True
    error = False

    for p in function : 
        if p == 'R' :
            reverse = not reverse
        elif p == 'D' :
            if len(num_list) == 0 :
                print("error")
                error = True
                break
            else : 
                if reverse : 
                    num_list.popleft()
                else : 
                    num_list.pop()

    if not error : 
        if not reverse : 
            num_list.reverse()
        print("[" + ",".join(map(str, num_list)) + "]")