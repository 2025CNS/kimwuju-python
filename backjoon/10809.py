lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
x = input()
s = 0

for i in lst:
    if i in x:
        print(x.index(i), end=' ')
    else:
        print(-1, end=' ')