N, X = map(int, input().split())
li = []
while True:
    A = list(map(int, input().split()))
    if len(A) == N:
        break
for i in range(N):
    if A[i] < X:
        li.append(A[i])
for i in range(len(li)):
    print(li[i], end=' ')