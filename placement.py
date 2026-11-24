n=int(input("Enter the number of students: "))
s=[]
sum=0
count=0
for i in range (n):
    
    name=input("Enter name of " + str(i+1) + ": ")
    asc=int(input("Enter assessment score of " + str(i+1) + ": "))
    s.append(( name, asc))
    
for i in range(0, n):
    sum+=s[i][1]
avg=sum/n
print("Average Score is : " + str(avg))



for i in range(n):
    for j in range(n-1-i):
        if s[j][1]<s[j+1][1]:
            s[j], s[j+1] = s[j+1], s[j]
    if s[i][1]<avg:
        count+=1
            
print(" Highest Score is : " + str(s[0][1]))
print("Lowest Score is : " + str(s[n-1][1]))
print("Number of students below average score is : " + str(count))
print("Second highest score is : " + str(s[1][1]))

for i in range(n):
    
    if s[i][1]<40:
        print("Name of student with score below 40 is : " + str(s[i][0]) + " and score is : " + str(s[i][1]))







