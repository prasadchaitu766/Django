def sample(a,b):
    c=a*b
    return c
s=sample(41,25)
print(s)
def sample():
    no=0
    no=+1
    yield (no)
    no+=1
    yield (no)
    no+=1
    yield (no)
s=sample()
print(s)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
