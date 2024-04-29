import sys
sys.stdin = open("Baekjoon/test.txt", "r")

input = sys.stdin.readline
n, m = map(int, input().split())

# union-find 자료구조를 이용하여 풀이해야 한다.
# 트리 자료구조

num_list = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]

def union(parent, x, y, rank) :
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x == root_y : 
        return
    if rank[root_x] < rank[root_y] :
        parent[root_x] = root_y
    else : 
        parent[root_y] = root_x
        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1

def find(parent, x) :
    if parent[x] == x : 
        return x
    # 경로 압축 -> find 하면서 만나는 모든 값의 부모노드를 root 로 만들어버림
    parent[x] = find(parent, parent[x])
    return parent[x]

for i in range(m) :
    _, a, b = map(int, input().split())
    if _ == 0 :
        union(num_list, a, b, rank)
    elif _ == 1 :
        # print(find(num_list, a))
        # print(find(num_list, b))
        if find(num_list, a) == find(num_list, b) : 
            print("YES")
        else : 
            print("NO")
        # print(num_list)