for i in range(1,6):
    for k in range(i, 6):
        print("*",end=" " )
    for j in range(2*(i-1)):
        print(" ", end=" ")
    for l in range (i, 6):
        print("*", end=" ")
    print()