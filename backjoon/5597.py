lst = []
for i in range(28):
    n = int(input())
    lst.append(n)
    lst.sort()
for j in range(1,31):
    if j in lst:
        continue
    else:
        print(j)