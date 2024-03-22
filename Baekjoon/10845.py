import sys
sys.stdin = open("Baekjoon/test.txt", "r")

from collections import deque

n = int(input())
que = deque([])

def push(x) : 
    que.append(x)
    return que

def pop() :
    if len(que) > 0 :
        print(que[0])
        return que.popleft()
    else : 
        return print(-1)
    
def size() :
    return print(len(que))

def empty() :
    if len(que) == 0 : 
        return print(1)
    else : 
        return print(0)
    
def front() :
    if len(que) == 0 :
        return print(-1)
    else :
        return print(que[0])
    
def back() : 
    if len(que) == 0 :
        return print(-1)
    else : 
        return print(que[-1])
    
for i in range(n):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == 'push' :
        push(int(cmd[1]))
    elif cmd[0] == 'pop' :
        pop()
    elif cmd[0] == 'size' :
        size()
    elif cmd[0] == 'empty' :
        empty()
    elif cmd[0] == 'front':
        front()
    elif cmd[0] == 'back':
        back()