#creating a function:
def function_name():
    '''body 
    any code you want to repeat 
    you can print ans as
    print(ans)
    or return 
    return ans'''
def sum():
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    c=a+b
    print(c)
#sum()   # function calling

#PASSING ARGUMENTS
def sum1(a,b):
    
    c=a+b
    print(c)
#sum1(13, 45)   # function calling

#using return keyword, to return teh value back at the atarting point
def sum2(a,b):
    
    c=a+b
    return(c)

sum2(13, 45)   # function calling

def sum():
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    c=a+b
    return(c)

# 1. No args and no return
# 2. args but no return
# 3. args with return
# 4. no args with return

