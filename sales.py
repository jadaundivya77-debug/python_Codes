p=int(input("enter: "))
sales=[]
for i in range(p):
    s=int(input("Enter sales: "))
    sales.append(s)
max=sales[0]
min=sales[0]
for i in sales:
    if i>max:
        max=i
    if i<min:
        min=i
print("max=", max)
print("min= ", min)