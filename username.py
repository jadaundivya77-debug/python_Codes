name=input("Enter your name : ")
roll=input("Enter your roll number : ")
def username(name, roll):
    a=name.split()
    return(a[0]+ a[1][0]+roll[0])
print(username(name, roll))