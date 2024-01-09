# 소수의 개수

# 소수 : 나눴을 때 인수가 1과 자기 자신 뿐! .... 근데 제한시간도 있음?

import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

# def decimal(x) :
#     dec_sum = []
#     for i in range(1, x+1):
#         if (x % i == 0):
#             dec_sum.append(i)
#     if len(dec_sum) == 2:
#         return x
#     else : 
#         return None
    
# cnt = 0

# for i in range(1, n+1):
    
#     if decimal(i) == i : 
#         cnt += 1
    
# print(cnt)



### solution

# 자연수 n이 입력되면 1부터 n까지 숫자 중 소수가 몇개인지 출력하는 문제
# 소수를 구할 때 가장 빠른 방법은 에라토스테네스 체를 이용하는 것

# ch = list([0]*n)
ch = [0]*(n+1)
cnt = 0
# print(ch)

for i in range(2, n+1) :
    if ch[i] == 0 :
        cnt += 1
        for j in range(i, n+1, i) :
            # range 에서 step 인자를 추가해주면 됨. (start, end, step)
            ch[j] = 1

print(ch)
