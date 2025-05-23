X = int(input())
N = int(input())

n=0

re=[]

while n<N:
    a,b=map(int,input().split())
    re.append(a*b)
    n+=1
re=sum(re)

if re==X:
    print('Yes')
else :
    print('No')