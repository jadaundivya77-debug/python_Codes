list=[10, 20, 10, 30, 20, 40]
list1=[]
for n in list:
    if n not in list1:
        list1.append(n)
print(list1)