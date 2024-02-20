import sys
sys.stdin = open("test.txt", "r")


n = int(sys.stdin.readline())

cnt = 0

# 그리디 풀이법

while n > 0 : 

    if n == 1 : 
        print(cnt)
        break

    elif n % 3 == 0 : 
        cnt += 1
        n //= 3
        # print(cnt)

        if n == 0 :
            n += 1

    elif (n+2) % 3 == 0 :
        n -= 1
        cnt +=1

    elif n % 2 == 0 : 
        cnt += 1
        n //= 2
        
        if n == 0 :
            n += 1