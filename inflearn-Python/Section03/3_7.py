import sys
sys.stdin = open("input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# sum = 0

# s = e = n//2
# for i in range(n):
#     sum += a[i][s]

#     s -= 1
#     e += 1
#     print(sum)

### solution
    
res = 0

s=e=n//2

for i in range(n) :
    for j in range(s, e+1):
        res += a[i][j]
        print(a[i][j])
    if i < (n//2):
        s -= 1
        e += 1
    else :
        s += 1
        e -= 1
for i in a :
    print(i)
print(res)
    

