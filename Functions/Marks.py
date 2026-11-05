def marks():
    n=[]
    s=0
    count=0
    no=int(input("Enter the number of students: "))
    for i in range(no):
        a=int(input("Enter the marks of student: "))
        n.append(a)
    for i in n:
        s+=i
    avg=s/no
    print("The average marks of the class is: ", avg)
    for i in n:
        
        if i>avg:
            print("The marks higher than average are: ", i)
            count+=1
    print("Number of marks more than average: ", count)


marks()
        
