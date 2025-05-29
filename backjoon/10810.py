N, M = map(int,input().split())
lst = [0] * (N)
for x in range(1, M+1):
    i, j, k = map(int, input().split())
    for v in range(i-1, j):
        del lst[v]
        lst.insert(v, k)
print(*lst)