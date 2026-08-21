l1=[10, 20, 30, 45, 67]
l2 = [10, 67, 30, 70, 20]
l3=[]
for i in l1:
    
    if i in l2:
        l3.append(i)
print(l3)