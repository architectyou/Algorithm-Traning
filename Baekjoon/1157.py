import sys
sys.stdin = open("Baekjoon/test.txt", "r")

input = sys.stdin.readline

# 단어공부(구현)

# alpha_list = [0] * 26
# alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# word = list(input().lower().rstrip())

# for i in word : 
#     idx = alpha.index(i)
#     alpha_list[idx] += 1

# # 리스트에서는 최댓값이 여러개라면, 여러개를 모두 리턴하는 것이 아닌 리스트에서 가장 앞에 있는 값이 리턴된다.
# result = []
# for i in range(len(alpha_list)) :
#     if alpha_list[i] == max(alpha_list) :
#         result.append(alpha[i].upper())

# if len(result) == 1 :
#     for i in result :
#         print(i)

# else :
#     print("?")


####
# user solution

w = input().upper()
s = list((set(w)))
cnt = []


for k in s : 
    cnt.append(w.count(k))
if cnt.count(max(cnt)) > 1 :
    print("?")
else : 
    print(s[cnt.index(max(cnt))])