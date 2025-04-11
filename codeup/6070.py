a=int(input())
if a==12 or a==1 or a==2:
    print('winter')
elif a//3==1 and a<=5:
    print('spring')
elif a//6==1 and a<=8:
    print('summer')
elif a//9==1 and a<=11:
    print('fall')