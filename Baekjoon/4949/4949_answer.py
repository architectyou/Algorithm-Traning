import sys
sys.stdin = open("Baekjoon/test.txt", "r")

while True : 
    line = sys.stdin.readline().rstrip() # 한줄씩 입력받기
    if line == "." :
        break

    stack = []
    balanced = True

    for i in line : 
        if i in "[(" :
            stack.append(i)
        elif i == ']' :
            if not stack or stack[-1] != "[" :
                balanced = False
                break
            stack.pop()
        elif i == ")" :
            if not stack or stack[-1] != "(" :
                balanced = False
                break
            stack.pop()
        
    if balanced and not stack : 
        print("yes")
    else : 
        print("no")