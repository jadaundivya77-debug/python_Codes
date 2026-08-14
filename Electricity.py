for i in range (1,6):
    unit= int(input(  "Enter the number of units consumed by customer " + str(i) + ": " ))
    if unit<=100:
        
        bill=unit*5
        print("Your electricity bill is: ",bill)
    elif unit<=200:
    
        bill=100*5+(unit-100)*7
        print("Your electricity bill is: ",bill)
    else:
    
        bill=100*5+100*7+(unit-200)*10
        print("Your electricity bill is: ",bill)