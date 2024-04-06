import sys
sys.stdin = open("Baekjoon/test.txt", "r")

a, b, v = map(int, input().split())

print(a, b, v)

# 반복문으로 풀이시 시간초과

if a >= v :
    print(1)

else : 
    # 하루에 올라갈 수 있는 양 (a-b)
    if (v-a)%(a-b) == 0 :
        print((v-a) // (a-b) + 1)
    # 마지막날에는 미끄러지지 않으므로 마지막에 올라가는 거리는 a
        # 마지막에 a만큼 한번 더 가야하므로 +1
    # 따라서 전체 올라가야 하는 거리는 v-a
    else : 
        # 나머지만큼 한번 더 가고 + a 만큼 한번 더 가야하므로
        print((v-a) // (a-b) + 2)