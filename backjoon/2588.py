a = int(input())
b = int(input())

c=b//10

d=c*10

e=b-d

f=c//10

g=f*100

h=(b-g-e)//10

re1=a*e

re2=a*h

re3=a*f

print(re1)
print(re2)
print(re3)

re2*=10

re3*=100

re4=re1+re2+re3

print(re4)