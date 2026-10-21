list= [25, 20, 30, 40, 50]
countEven=0
countOdd=0
for i in range(0, len(list)):
    if list[i]%2==0:
        countEven+=1
    else:
        countOdd+=1
print("Total number of even in the list is: ", countEven)
print(" Total number of odd is: ", countOdd)