t=int(input())
for i in range(1,t+1):
    if i==1:
        print(0)
    elif i==2:
        print(6)
    elif i==3:
        print(28)
    elif i==4:
        print(96)
    else:
        x= (((i**2) *(i**2 -1)) -(48 + (i-4)*16 + (i-4)*24 + ((i-4)**2)*8 ))/2
        print(int(x))