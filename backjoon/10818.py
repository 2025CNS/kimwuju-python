N = int(input())
a = 0
li = []

while True:
    li = list(map(int,input().split()))
    a += len(li)
    if a == N:
        li.sort()
        print(li[0],li[N-1])
        break