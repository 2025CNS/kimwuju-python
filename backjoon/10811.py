N,M = map(int,input().split())
lst = [i for i in range(1, N+1)]
li = []
for i in range(M):
    a, b = map(int, input().split())
    if a == b:
        continue
    li = lst[a-1:b]
    li.reverse()
    lst[a-1:b] = li
print(*lst)