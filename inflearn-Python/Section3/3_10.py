import sys
sys.stdin = open("input.txt", "r")

# 스도쿠 검사
# a = [list(map(int, input().split())) for _ in range(9)]

# row = [0]*10
# column = [0]*10
# box = [0]*10
# cnt = 0
# # print(row)
# for i in range(9):
#     for j in range(9):
#         row[a[i][j]] = 1
#         column[a[i][j]] = 1
    

#     if sum(row) and sum(column) and sum(box) == 9 : 
#         cnt += 1
#     else : 
#         None

# if cnt == 9 :
#     print("YES")
# else : 
#     print("NO")

#### solution
    
def check(a):
    for i in range(9):
        #열과 행 테스트하기
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1) != 9 or sum(ch2) != 9 :
            return False
    # 3 by 3 격자 테스트 하기
    for i in range(3):
        for j in range(3):
            ch3 = [0]*10 
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9 :
                return False
            
    return True

a = [list(map(int, input().split())) for _ in range(9)]


# True를 return 하면 YES를 출력하고, False를 return 하면 NO를 출력함.
if check(a):
    print("YES")
else :
    print("NO")