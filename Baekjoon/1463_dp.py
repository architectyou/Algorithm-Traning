import sys
sys.stdin = open("test.txt", "r")

n = int(input())
d = [0] * (n+1)

for i in range(2, n+1):
    
    d[i] = d[i-1] + 1

    if i % 3 == 0 :
        d[i] = min(d[i], d[i//3] + 1)
    if i % 2 == 0 :
        d[i] = min(d[i], d[i//2] + 1)


print(d[n])


## 타 답안

d = {1:0, 2:1}

def s(n : int) -> int : 
    if n in d : 
        return d[n]
    t = 1 + min(s(n//3) + n % 3, s(n//2) + n % 2)
    d[n] = t
    return t

print(s(int(sys.stdin.readline())))