a=[1,4,2,5]
max=0
for i in a:
    if i>max:
        max=i
for i in range(1,max+1):
    if i not in a:
        print(i)
