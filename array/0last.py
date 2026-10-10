from array import array
a= array("i",[10, 0, 20, 0, 2, 0, 0, 19])
for i in a:
    if i == 0:
        a.remove(i)
        a.append(i)
print(a)