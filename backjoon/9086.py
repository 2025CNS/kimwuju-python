n = int(input())

a = 0
while True:
    w = input()
    a += 1
    T = len(w)
    print(w[0]+w[T-1])
    if a == n:
        break