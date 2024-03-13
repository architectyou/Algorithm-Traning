# import sys
# sys.stdin = open("coursera/test.txt", "r")

# n = int(input())
# num_list = list(map(int, input().split()))

def faster_max_pairwise(num_list):
    if num_list[0] > num_list[1] : 
        max1, max2 = num_list[0], num_list[1]
    else : 
        max1, max2 = num_list[1], num_list[0]

    for num in num_list[2:]:
        if num > max1 : 
            max2 = max1
            max1 = num

        elif num > max2 : 
            max2 = num

    return max1 * max2

if __name__ == '__main__' :
    _ = int(input())
    input_nums = list(map(int, input().split()))
    print(faster_max_pairwise(input_nums))

# print(faster_max_pairwise(num_list))