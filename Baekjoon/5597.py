import sys
sys.stdin = open("Baekjoon/test.txt", "r")

student = [num for num in range(1, 31)]

for i in range(28) :
    n = int(input())
    if n in student : 
        student.remove(n)

for i in student : 
    print(i)