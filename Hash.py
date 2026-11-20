s=input("Enter the string : ")
l=[]
def hash(s):
    a=s.split()
    for i in a:
        if i.startswith("#"):
            l.append(i)
    return l

print(hash(s))


