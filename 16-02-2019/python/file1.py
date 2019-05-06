try:
    with open("sample.txt","r") as file:
        f=file.read()
        print(f)
except FileNotFoundError as fe:
    print(fe)
