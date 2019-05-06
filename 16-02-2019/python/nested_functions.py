def outer(a,b):
    c=a+b
    print(c)
    def inner(d,e):
        x=d-e
        print(x)
    inner(56,45)
outer(25,36)
