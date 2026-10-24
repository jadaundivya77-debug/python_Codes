def fact():
    n=int(input("Enter the number: "))
    p=1
    for i in range(1, n+1):
        p*=i
    return(p)

print(fact())
