a=[[1,2,3], [4,5,6], [7,8,9]]

for i in range(3):
    s=0
    for j in range(3):
        s+=a[i][j]
    print("Sum of", i+1, "row is : ", s)