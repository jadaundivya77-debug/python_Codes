

for i in range (1,6):
    for j in range(1, i+1):
        print("*", end=" ")

    for k in range(2*(5-i)):
        print(" ", end=" ")
    
    


    for k in range(1,i+1):
            print("*", end=" ")
    print()


for i in range (1,6):
    for j in range (i, 6):
            print("*", end=" ")

    for k in range(2*(i-1)):
        print(" ", end=" ")

    for k in range (i, 6):
        print("*", end=" ")
    print()
    