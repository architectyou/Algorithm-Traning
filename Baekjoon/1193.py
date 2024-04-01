import sys
sys.stdin = open("Baekjoon/test.txt", "r")

# 분수 찾기
x = int(input())

line = 1

print(x)

while x > line :
    x -= line
    line += 1

# 규칙
up = 1
down = 1
res = []
# line이 홀수인 경우 -> 분자는 줄어들고, 분모는 커짐
# line이 짝수인 경우 -> 분자는 늘어나고, 분모는 작아짐
if line == 1 :
    res.append((up, down))

elif line % 2 == 0 :
    down = line
    res.append((up, down))
    for i in range(line-1) :
        up += 1
        down -= 1
        res.append((up, down))

else : 
    up = line
    res.append((up, down))
    for i in range(line-1) :
        up -= 1
        down += 1
        res.append((up, down))

print(x)
print(line)
print(res)
print(res[x-1][0],"/",res[x-1][1], sep = "")