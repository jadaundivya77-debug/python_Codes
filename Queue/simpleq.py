q=[0]*5
f=-1
r=-1
def enqueue():
    global f,r
    if r == len(q)-1:
        print("Queue is overflow, no more insertion can be done.")
    else:
        value= int(input("Enter the value to be inserted: "))
        if f==-1:
            f=0
        r=r+1
        q[r]=value
        print("Value inserted successfully")

def dequeue():
    global f,r
    if f==-1:
        print("Queue is underflow, no more deletion can be done.")
    if f>r:
        f=-1
        r=-1
        print("Queue is now empty.")
    else:
        f=f+1
        print("Value deleted successfully")

def peek():
    global f,r
    if f==-1:
        print("Queue is empty, no elements to peek.")
    else:
        print(f"Front element is: {q[f]}")

def display():
    global f,r
    if f==-1:
        print("Queue is empty, no elements to display.")
    else:
        print("Elements in the queue are:")
        for i in range(f,r+1):
            print(q[i])


while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print ("4. Display")
    print("5. Exit")
    ch= int(input("enter your choice: "))
    if ch==1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        peek()
    elif ch==4:
        display()
    elif ch==5:
        break
    else:
        print("Invalid choice, please try again.")
        

