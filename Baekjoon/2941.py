import sys
sys.stdin = open("Baekjoon/test.txt", "r")

words = sys.stdin.readline().rstrip()

cro = ["c=", "c-", "dz=", "d-", "d-", "lj", "nj", "s=", "z="]

for i in cro :
    ## 일치하는 단어가 있을 때마다 변경
    words = words.replace(i, 'a')

print(len(words))