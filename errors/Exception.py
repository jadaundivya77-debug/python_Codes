#Exception Handling in Python
#Exception handling is a mechanism to handle runtime errors, allowing the program to continue its execution instead of crashing. 
# In Python, exceptions can be handled using try and except blocks.  


#try:
    #Risky Code
#except:
    #Exception Handling Code

'''try:
    a=10
    b=0
    result=a/b
    print("Result:", result)
except: 
    print("An error occured")'''

#user defined Exceptions: In Python, you can also create your own custom exceptions by defining a new class 
# that inherits from the built-in Exception class.


#Bulit-in Exceptions in Python
# 1. ZeroDivisionError: Raised when a division by zero occurs.
# example: 10/0

#2. NameError: Raised when a variable is not defined.
#example: print(x) where x is not defined

#3. TypeError: Raised when an operation is performed on an object of an inappropriate type.
#example: "5" + 5, int + str

#4. ValueError: Raised when a function receives an argument of the correct type but an inappropriate value.
#example: int("hello")

#5. IndexError: Raised when an index is out of range for a sequence.
#example: my_list = [1, 2, 3]; print(my_list[5])

#6. KeyError: Raised when a key is not found in a dictionary.
#example: my_dict = {"a": 1, "b": 2}; print(my_dict["c"])

#7. AttributeError: Raised when an attribute reference or assignment fails.
#example: 5.append(10) #int object has no attribute 'append'

#8. FileNotFoundError: Raised when a file or directory is requested but cannot be found.
#example: open("xyz.txt") #file does not exist

#9. ImportError: Raised when an import statement fails to find the module definition or when a from 
# ... import fails to find a name that is to be imported.
#example: import non_existent_module

#10. ModuleNotFoundError: Raised when a module could not be found.
#example: import non_existent_module




#A single block of code can have multiple except statements to handle different exceptions.
'''try:
    a=10
    b=int("h")
    result=a//b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid value.")'''


#finally block: The finally block is used to define a block of code that will be executed
#   regardless of whether an exception occurred or not.
#Except exception as e: The except exception as e syntax allows you to capture the 
# exception object and access its attributes or methods for further analysis or logging.


try:
    a=10
    b="00"
    result=a/b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid value.")
except Exception as e:
    print("Ohh NO")
finally:
    print("Mwahahaha, chal nikal yahaan se. Ye mera ghar hai, tu yahan kaise aa gaya?")

#raise ValueError("This is a custom error message.")
age=int(input("Enter your age: "))
if age<18:
    raise ValueError("Age must be at least 18.")
print("You are eligible to vote.")