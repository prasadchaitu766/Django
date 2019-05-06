number=int(input("enter first number"))
# Second=int(input("enter Second number"))
i=0
first=0
second=1
while(i<number):
    if(i<-2):
        Next=1
    else:
        Next=first+second
        first=second
        second=Next
    print(Next)
    i=i+1
