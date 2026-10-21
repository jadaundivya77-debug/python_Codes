maximum=0
for i in range (1,6):
    
    purchase= int(input(  "Enter the purchase amount of customer " + str(i) + ": " ))
    if purchase >= 10000:
        discount = float(purchase*0.20)
        print("Your discount is: ",discount)
    elif purchase >= 5000:
        discount = float(purchase*0.10)
        print("Your discount is: ",discount)
    elif purchase>=2000:
        discount = float(purchase * 0.05)
        print(" Your discount is :", discount)
    else:
        discount=0
        print("Your discount is: ",discount)
    if discount>maximum:
        maximum=discount
print("The maximum discount is: ",maximum)
    
    
    