A, B = input().split()
lst1 = []
lst2 = []
for i in range(3):
    lst1.append(A[i])
    lst2.append(B[i])
lst1.reverse()
lst2.reverse()
A = ''.join(lst1)
B = ''.join(lst2)
if A > B:
    print(A)
elif A < B:
    print(B)