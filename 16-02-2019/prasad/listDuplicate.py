list=[2,4,5,6,7,8,9,2,3,4,5,4,3]
list1=[]
for x in list:
    if x not in list1:
        t=list1.append(x)
print(list1)