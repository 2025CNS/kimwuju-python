N, M = map(int,input().split())
lst = []
for y in range(1, N+1):
    lst.append(y)

for x in range(M):
    i, j = map(int, input().split())
    if i != j: 
        a = lst[i-1]
        b = lst[j-1]
        lst.remove(a)
        lst.remove(b)
        lst.insert(i-1, b)
        lst.insert(j-1, a)

print(*lst)