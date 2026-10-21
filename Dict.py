#Dictionary is a collection of key-value pairs
students={ "Sandhya":400, "Rahul":350, "Priya":450 }
# printing keys of the dictionary
print(students.keys())
#printing values of the dictionary
print(students.values())
#add a new key
students["Mahak"]=400
print(students)
#Change the value of a key
students["Rahul"]=500
print(students)
#Using get() method to access the value of a key
print(students.get("Divya"))  #if the key is not present it will return None
#default value can be set using get() method
print(students.get("Divya", "Not Found"))  #if the key is not present it will return "Not Found"

#If we put 2 same keys with different values, the last value will be considered
dict= {"a":1, "b":2, "c":3, "a":4}
print(dict)  #Output: {'a': 4, 'b': 2, 'c': 3}