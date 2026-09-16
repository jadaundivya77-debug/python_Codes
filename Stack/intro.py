stack = []
#Stack is a data structure that follows the Last In First Out (LIFO) principle. It means that the last element added to the stack
#  top = -1     will be the first one to be removed.
#top ++, top = 0, then s[top] = element 
#insert an element in the stack is called push operation and remove an element from the stack is called pop operation.
# peek operation is used to get the top element of the stack without removing it.
# exit operation is used to check if the stack is empty or not.
# overflow happens when we try to push an element into the stack when it is already full. 
# Underflow happens when we try to pop an element from the stack when it is empty.  
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = int(input("Enter the element to be pushed: "))
        stack.append(element)
        print(f"{element} pushed to stack")
    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty, cannot pop")
        else:
            popped_element = stack.pop()
            print(f"{popped_element} popped from stack")
    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty, cannot peek")
        else:
            top_element = stack[-1]
            print(f"Top element is {top_element}")
    elif choice == 4:
        break
    else:
        print("Invalid choice, please try again.")



stack=[]
while True:
    
    print("1. Push")
    print("2. pop")
    print("3. peek")
    print("4. exit")
    choice= int(input("enter the chocie: "))
    if choice ==1:
        element = int(input("Enter the Element : "))
        stack.append(element)
        print(f"{element} pushed to stack")
    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty, cannot pop")
        else:
            pop_element = stack.pop()
            print(f"{pop_element} popped from stack")
    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty, cannot peek")
        else:
            top_element = stack[-1]
            print(f"Top element is {top_element}")
    elif choice == 4:
        break
    else:
        print("Invalid choice, please try again.")
