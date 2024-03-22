def solution(n):
    answer = 0

    n_list = list(str(n))

    for i in n_list : 
        i = int(i)
        answer += i


    return answer


### 재귀 구조 이용하기

def sum_digit(num) :
    '''number의 각 자리수를 더해서 return 하기'''
    if num < 10 : 
        return num
    
    # 재귀에서 각가긔 자릿수를 10으로 나눈 나머지를 이용해 그대로 더하는 방식
    return num % 10 + sum_digit(num // 10)

print("결과 : {}".format(sum_digit(456)))