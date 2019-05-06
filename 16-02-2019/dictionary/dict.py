d1={101:{"name":"prasad","marks":[60,65,87]},
    102:{"name":"naidu","marks":[90,85,80]},
    103:{"name":"ramu","marks":[40,70,50]}}
d2=d1.values()
lst=[]
for x in d2:
    d3=x['marks']
    d4=sum(d3)
    d5=lst.append(d4)
for y in lst:
    print(y)

