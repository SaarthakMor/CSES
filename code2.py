x=int(input())
y=input()
numbers=[]
for num in y.split():
    numbers.append(int(num))
numbers.sort()
for i in range(0,x-1):
    if numbers[x-2] == x-1:
        print(x)
        break
    if numbers[i] != i+1:
        print(i+1)
        break


    



