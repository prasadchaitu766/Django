# lidt=[2,3,4,4,2,3,6,7,9]
# r=set(lidt)
# print(r)
lidt=[2,3,4,4,2,3,6,7,9]
k=[]
for x in lidt:
    if x  not in k:
        k.append(x)
print(k)