s="Satyam Shivam Sundaram"
t="satYam shivam Sundaram"
s1=s.upper()
print(s1)

s2=s.lower()
print(s2)

s3=s.title()
print(s3)

s4=s.capitalize()
print(s4)

print(s.swapcase())

#when you want to compare two strings without considering the case, you can use casefold() method.
print(s.casefold() )
if s.casefold() == t.casefold():
    print("Both are same")
else:
    print("Both are different")

# to remove the spaces from the beginning and end of the string, you can use the strip() method.
space= "Satyam shivam Sundaram   "
print(space.strip())

#to remore left or right spaces from the string, you can use lstrip() and rstrip() methods.
print(space.lstrip())
print(space.rstrip())
#if we pass any character in strip() method, it will remove that character from the beginning and end of the string.
print(space.strip('S'))

#find function is used to find the index of the first occurrence of a substring in a string.
#  If the substring is not found, it returns -1.
print(s.find("shivam"))
print(s.find("f"))

#index() function is used to find the index of the first occurrence of a substring in a string.
# If the substring is not found, it raises a ValueError.
print(s.index("Shivam"))
#print(s.index("f"))  # This will raise a ValueError since "f"

# The count() method is used to count the number of occurrences of a substring in a string.
print(s.count("a"))
# startswith() method is used to check if a string starts with a specified substring. 
print(s.startswith("Satyam"))

#replace() method is used to replace a specified substring with another substring in a string.
print(s.replace("a", "aa"))

# split function is used to convert the string into the list
print(s.split())

#join() this function converts the list to a string
l=['Divya', 'Mahak', 'Sandhya']
results= " ".join(l)
print(results)

# isalpha function checks if there isalphabet or not?
print("Mahak".isalpha()) #TRUE
print(s.isalpha())   #False

#isallnum is numbers
#isspace checks if there is space or not
print(s.isspace())  #pta nhi
#islower
print(s.islower())
print(s.isupper())
print(s.istitle())