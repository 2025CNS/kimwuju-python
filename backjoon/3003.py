lst = [1, 1, 2, 2, 2, 8]
li = []

ma = list(map(int,input().split()))

for i in range(len(lst)):
    if lst[i] != ma[i]:
        li.append(lst[i] - ma[i])
    else:
        li.append(0)
print(*li)