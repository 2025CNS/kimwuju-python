a, b = map(int,input().split())

if a!=0:
    if b>45:
        print(a,b-45)
    elif b<45:
        print(a-1,15+b)
    else :
        print(a,0)
elif a==0:
    if b>45:
        print(a,b-45)
    elif b<45:
        print(23,15+b)
    else :
        print(a,0)