import sys
sys.stdin = open("input.txt", "r")

n = int(input())
num_list = list(map(int, input().split()))


def reverse(x):

    num_digit = list(str(x))
    digit_list = []
    num = 0

    for i in range(len(num_digit)):
        a = x // (10**(len(num_digit)-(i+1)))
        x = x - a * (10**(len(num_digit)-(i+1)))
        
        num += a * (10**(i))
        num = int(num)
    
    return num

def isPrime(x):
    for i in range(2, x) :
        if x % i == 0 :
            return False
    return True

for i in num_list :
    rev_i = reverse(i)
    if isPrime(rev_i) == True : 
        print(rev_i, end=" ")