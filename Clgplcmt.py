n=int(input("Enter the number of students: "))
s=[]
for i in range (n):
    Roll_no=int(input("Enter Roll number of " + str(i+1) + ": "))
    name=input("Enter name of " + str(i+1) + ": ")
    asc=int(input("Enter assessment score of " + str(i+1) + ": "))
    s.append((Roll_no, name, asc))
for i in range(n-1):
    for j in range(n-1-i):
        if s[j][2]<s[j+1][2]:
            s[j], s[j+1] = s[j+1], s[j]
        if s[j][2]==s[j+1][2]:
            if s[j][0]>s[j+1][0]:
                s[j], s[j+1]=s[j+1], s[j]

print("Roll No. Name Assessment Score")
for i in range(n):
    print(s[i][0], "    ",  s[i][1], "    ",  s[i][2])



search=int(input("Enter roll number of the student you want : "))
for i in range(n):
    if search==s[i][0]:
        print("Roll no. : ", s[i])
        break
    else:
        print("Invalid Roll number")
