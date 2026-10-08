stu= int(input("enter number of students: "))
marks= []
passed=0
fail=0
for i in range(stu):
    m=int(input("enter= "))
    marks.append(m)

for i in marks:

    if i>=35:
        passed+=1
    else:
        fail+=1
print("Passed student: ", passed)
print("failed students: ", fail)

