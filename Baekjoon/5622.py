import sys
sys.stdin = open("Baekjoon/test.txt", "r")

word = list(sys.stdin.readline().rstrip())

# print(word)

# time = 0

# for i in word :
#     if i in 'ABC' : 
#         time += 3
    
#     elif i in 'DEF' :
#         time += 4
    
#     elif i in 'GHI' :
#         time += 5
    
#     elif i in 'JKL' :
#         time += 6
    
#     elif i in 'MNO' :
#         time += 7
    
#     elif i in "PQRS" :
#         time += 8
    
#     elif i in "TUV" :
#         time += 9
    
#     elif i in "WXYZ" :
#         time += 10
    

# print(time)


## claen code

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
arr = input()
result = 0

for i in range(len(arr)) :
    for j in dial :
        if arr[i] in j :
            result += dial.index(j) + 3

print(result)