n=int(input("enter a number"))
for x in range(n,0,-1):
    for y in range(0,n-x+1):
        print(end=" ")
    for z in range(0,x+1):
        print("*",end=" ")
    print()