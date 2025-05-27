n = int(input())

a = 0

N = []

while n > a:
    N = list(map(int,input().split()))
    I = len(N)
    a += I

jum = int(input())

print(N.count(jum))