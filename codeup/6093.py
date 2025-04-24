n = int(input())

while True:
    k = list(map(int, input().split()))
    if len(k) == n:
        break

k.reverse()
print(*k)