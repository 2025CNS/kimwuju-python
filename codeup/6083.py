r,g,b = map(int,input().split())
for i in range(r):
    for j in range(g):
        for x in range(b):
            print(i,j,x)
print(r*g*b)