def CV():
    s=input("Enter the string: ")
    v=0
    c=0
    vov="AEIOUaeiou"
    for i in s:
        if i in vov:
            v+=1
        else:
            c+=1
    return( "Total Vowels= ", v ,"and total consoonants = ", c)

print(CV())

