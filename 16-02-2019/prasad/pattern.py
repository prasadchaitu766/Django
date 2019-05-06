number=int(input("enter a number:"))
for x in range(0,number):
    for y in range(0,number-x-1):
        print(end=" ")
    for z in range(0,x+1):
        print("*",end=" ")
    print()