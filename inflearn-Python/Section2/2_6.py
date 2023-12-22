import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())

num_list = input().split()
a = []
res = {}

def digit_sum(x) :
    return sum(x)

for i in num_list:
    for j in i :
        j = int(j)
        a.append(j)
    res[i] = digit_sum(a)
    a = []

sorted_res = sorted(res.items(), key = lambda x : x[1] ,reverse=True)

arrMin = float('-inf')

for i in range(len(sorted_res)):
    if sorted_res[i][1] > arrMin :
        arrMin = sorted_res[i][1]
        print(sorted_res[i][0])
        
        
# 문제는 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자를 출력하지 않음....


# solution1

# 숫자를 넘겨주면 자릿수를 구하는 def digit_sum(x)를 만들어야 함.

n = int(input())
a = list(map(int, input().split()))

# 각 자릿수의 합을 구하는 def 생성
def degit_sum(x) :
    sum = 0
    while x > 0 :
        sum += x%10
        x = x//10
    return sum
max = -214700000
for x in a : 
    tot = digit_sum(x)
    if tot > max :
        max = tot
        res=x
print(x)


### solution2

n = int(input())
a = list(map(int, input().split()))

def degit_sum(x) :
    sum = 0
    #정수를 str 처리해서 처리하기
    for i in str(x):
        sum += int(i)
    return sum
    
max = -214700000
for x in a : 
    tot = digit_sum(x)
    if tot > max :
        max = tot
        res=x
print(x)