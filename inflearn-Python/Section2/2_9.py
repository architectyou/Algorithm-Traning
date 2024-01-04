import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
num_dict = {}

for i in range(n):
    num = list(map(int, input().split()))
    res = {}
    for j in num :
        try : res[j] += 1
        except : res[j] = 1

    # key value를 호출 할 때 value를 기준으로 호출하는게 많다면 딕셔너리를 뒤집자.
    res_res = {v:k for k, v in res.items()}

    a = res_res.get(3)
    b = res_res.get(2)
    c = res_res.get(1)
    
    if a != None : 
        prize = 10000 + (a*1000)
        # print(f"3개다 맞춘경우? : {prize}" )
    elif b != None :
        prize = 1000 + (b*100)
        # print(f"2개다 맞춘경우? : {prize}" )
    elif c!= None : 
        num.sort(reverse=True)
        prize = num[0] * 100
        # print(f"1개다 맞춘경우? : {prize}" )

    num_dict[i+1] = prize

num_dict = sorted(num_dict.items(), reverse = True, key = lambda item : item[1])
print(num_dict[0][1])


### solution ###
res = 0

for i in range(n):
    tmp = input().split()
    # 문자열 리스트로 들어오게 됨.
    tmp.sort()
    a, b, c = map(int, tmp)

    # 가장 좋은 것을 if문으로 먼저 이용해야
    if a == b and b == c :
        money = 10000 + a * 1000
    elif a == b or a == c : 
        # 한 눈으로 변수를 잡아서 계산해야 하므로 a를 기준으로 판단.
        # if 구문에서 처음이 참이 되면 그 밑으로는 하지 않는다.
        money = 1000 + (a*100)
    elif b == c :
        money = 1000 + (b*100)
    else :
        money = c * 100

    if money > res : 
        res = money

print(res)