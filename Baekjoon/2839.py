import sys
sys.stdin = open("test.txt", "r")

n  = int(input())

cnt_5 = 0
cnt_3 = 0

while n > 0 :

    if n >5 :
        cnt_5 += (n//5)
        n %= 5

        if n % 3 == 0 :
            cnt_3 += (n//3)
            n %= 3

        else : 
            n = cnt_5 * 5 + n
            cnt_5 -= 1
            n -= cnt_5 * 5

            if n % 3 == 0 :
                cnt_3 += (n//3)
                n %= 3

            else : 
                print(-1)

    elif n % 3 == 0 :
        cnt_3 += (n//3)

    else : 
        print(-1)
        break

cnt = cnt_5 + cnt_3

if cnt != 0 :
    print(cnt)
