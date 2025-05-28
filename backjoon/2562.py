Max = 0
count = 0
li = []
for i in range(9):
    N = int(input())
    li.append(N)
    if N > Max:
        Max = N
for i in range(9):
    if li[i] == Max:
        count = i + 1
print(Max)
print(count)