p=open("File.txt", "w")
p.write("Hello! My name is Divya.\n")
p.write("I am a student of BCA.\n")
p.close()
'''p=open("File.txt", "r")
print(p.read())
p.close()'''

'''f=open("File.txt", "r")
d=f.read(10) #characters
print(d)
f.close()'''

'''f=open("File.txt", "r")
d=f.readline() #reads one line
d=f.readline()
print(d)
f.close()'''


'''f=open("File.txt", "r")
for line in f:
    print(line, end="")
f.close()'''

'''name=input("Enter your name : ")
age=input("Enter your age : ")
course=input("Enter your course : ")
f=open("File.txt", "a+")
f.write(f"Name: {name}, Age: {age}\n")
f.write(f"Course: {course}\n")'''

'''f.close()
f=open("File.txt", "r")
print(f.read())
f.close()'''



while True:
    print("1. Add Record")
    print("2. Display Record")
    print("Search")
    print("Delete")
    print("Exit")
    choice=int(input("Enter your chocie: "))
    if choice==1:
        name=input("Enter your name : ")
        age=int(input("Enter your age : "))
        class_name= input("Enter your class : ")
        total_marks=int(input("Enter your total marks : "))
        f=open("File.txt", "a+")
        f.write(f"Name : {name}\n")
        f.write(f"Age : {age}\n")
        f.write(f"Class name : {class_name}\n")
        f.write(f"Total marks : {total_marks}\n")
        print("Student added successfully")
        f.close()
    if choice==2:
        f=open("File.txt", "r")
        print(f.read())
        f.close()
    

    


