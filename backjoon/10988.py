M = input()

lst = [i for i in M]
lst1 = [i for i in M]
lst1.reverse()
count = 0

for i in range(len(lst)):
    if lst[i] != lst1[i]:
        continue
    else:
        count += 1
if count == len(lst):
    print(1)
else:
    print(0)