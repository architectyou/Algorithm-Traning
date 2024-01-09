import sys
sys.stdin = open("input.txt", "r")

### 점수 계산

n = int(input())
ans = list(map(int, input().split()))
# ans.insert(0, 0)

# score = 0
# cnt = 0

# for i in range(1, len(ans)) :
#     if ans[i-1] == 0 and ans[i] == 1 :
#         score += 1
#     elif ans[i-1] == 1 and ans[i] == 1 :
#         cnt += 1
#         score += cnt
#         print(score)

# print(cnt)
# print(score)

sum = 0
cnt = 0

for x in ans :
    if x == 1 :
        cnt += 1
        sum += cnt
        print(cnt)
    else : 
        cnt = 0

print(cnt)
print(sum)