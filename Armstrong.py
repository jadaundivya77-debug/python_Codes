for i in range (100, 1000):
    x=i
    p=0
    while i>0:
        d=i%10
        p= p + d**3
        i=i//10
    if p==x:
        print(x)
