import sys
sys.stdin = open("Baekjoon/test.txt", "r")

### 1874 스택 수열
n = int(input())

## 정답수열
answer = [int(input()) for _ in range(n)]

stack = []
result = []
## 정답과 비교하여 채워넣기
num = 1

for i in answer:
    while num <= i:
        stack.append(num)
        result.append("+")
        num += 1
    if stack[-1] == i:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        break
else:  # for-else 구문 사용, break 없이 for 루프가 정상적으로 종료되면 실행됨
    for op in result:
        print(op)
