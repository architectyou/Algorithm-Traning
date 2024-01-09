import sys
# sys.stdin = open("input.txt", "r")

s = input()

res = 0

for x in s : 
    if x.isdecimal():
        x = int(x)
        res = res * 10 + x

res_list = []

for i in range(1, res + 1) :
    if res % i == 0 :
        res_list.append(i)

### 개수를 셀거라면

cnt = 0

for i in range(1, res+1):
    if res % i == 0 :
        cnt += 1

print(res)
print(len(res_list))