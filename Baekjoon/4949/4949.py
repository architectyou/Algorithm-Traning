import sys
sys.stdin = open("Baekjoon/test.txt", "r")

# 균형잡힌 세상
# stack

# 틀림 (why??....)

lines = sys.stdin.readlines()

for line in lines : 

    if line == "." :
        continue

    stack = []
    balanced = True

    for i in line : 
        if i in "[(" :
            stack.append(i)
        elif i == "]" :
            if not stack or stack[-1] != "[" :
                balanced = False
                break
            stack.pop()
        elif i == ")" :
            if not stack or stack[-1] != "(" :
                balanced = False
                break
            stack.pop()
    if balanced and not stack  :
        print("yes")
    else : 
        print("no")