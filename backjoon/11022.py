T=int(input())

n=0

x=1

while n<T:
    a,b=map(int,input().split())
    num=a+b
    n+=1
    print(f'Case #{x}: {a} + {b} = {num}')
    x+=1