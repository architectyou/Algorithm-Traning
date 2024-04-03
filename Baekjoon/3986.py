import sys
sys.stdin = open("Baekjoon/test.txt", "r")

n = int(input())

res = 0

for i in range(n) :
    word = list(sys.stdin.readline().rstrip())
    stack = []
    
    for j in word : 
        if len(stack) != 0 : 
            if stack[-1] == j :
                stack.pop()
            else : 
                stack.append(j)
        else : 
            stack.append(j)

    if len(stack) == 0 :
        res += 1

print(res)