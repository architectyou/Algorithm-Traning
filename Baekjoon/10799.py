import sys
sys.stdin = open("Baekjoon/test.txt", "r")

stick = list(sys.stdin.readline())
stack = []

stick_num = 0
res = 0

# 괄호의 스택 구조는 스택에 하나씩 넣고 ()쌍으로 빼서 -> cnt 변수로 세는 구조
for i in range(len(stick)) : 
    if stick[i] == '(' :
        stack.append(stick[i])
        # = 쇠 막대기의 시작?
    elif stick[i] == ')' :
        if stick[i-1] == '(' :
            stack.pop()
            # 자른 기준으로 앞의 막대 개수(머리개수)를 세면 몇 개 조각이 났는지 알 수 있음.
            res += len(stack)
        else : 
            stack.pop()
            stick_num += 1
            # 마무리 된 것만 하나로 추가해주기
            res += 1

print(res)