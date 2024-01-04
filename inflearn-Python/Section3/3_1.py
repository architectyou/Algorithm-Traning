import sys
# sys.stdin = open("input.txt", "r")

# 회문 문자열 검사

n = int(input())

for i in range(n) :
    
    word = list(input().upper())
    a = len(word) // 2

    if len(word) % 2 == 0 :
        if word[:a] == list(reversed(word[a:])) :
            print(f"#{i+1} YES")
        else :
            print(f"#{i+1} NO")
    else :

        if word[:a] == list(reversed(word[a+1:])) :
            print(f"#{i+1} YES")
        else :
            print(f"#{i+1} NO")
