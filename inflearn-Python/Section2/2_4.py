import sys
sys.stdin = open("input.txt", "rt")


n = int(input())
# num = list(map(int, input().split()))
a = list(map(int, input().split()))
# sum_score = 0

# for i in range(n):
#     sum_score += num[i]
    
# avg = round(sum_score / n)

# print(avg)
# print(num)


#### solution


avg = round(sum(a)/n)
# 최솟값을 저장하는걸 inf를 이용하려면 float만 가능함 int는 불가능.
min = float('inf')
# enumerate 이용
for idx, x in enumerate(a):
    # idx에는 index 값을 반환하고, x에는 index에 해당하는 값을 반환함.
    
    # tmp라는 변수를 만들어서 평균과 실제 값의 차이를 넣고 이 차이가 최소가 되는 값 (이 중간값이 될 예정) 을 찾는다.
    tmp = abs(x - avg)
    if tmp < min : 
        min = tmp
        score = x
        # 만약 여러 개가 있으면 그 중에 큰 점수를 말하라고 했으므로 점수도 저장하고 있어야 함.
        res = idx+1
        
    elif tmp == min : 
        if x > score :
            score = x
            res = idx+1
            
print(avg, res)




"""

대표값 문제 오류 수정
round는 round_half_even 방식을 택한다.

a = 4.500
print(round(a))

= 4가 된다.
정확히 반에 있다면 짝수쪽으로 근사값을 내준다...


"""