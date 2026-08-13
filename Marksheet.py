num1= int(input("Enter number of 1st subject: "))
num2= int(input("Enter number of 2nd subject: "))
num3= int(input("Enter number of 3rd subject: "))
num4= int(input("Enter number of 4th subject: "))
total= num1+num2+num3+num4
print("Total marks obtained: ", total)
percentage= (total/400)*100
print("Percentage: ", percentage )
if(percentage>=90):
    print("Grade: A")
elif(percentage>=80):
    print("Grade: B")
elif(percentage>=70):
    print("Grade: C")
elif(percentage>=60):
    print("Grade: D")
else:
    print("Grade: F")