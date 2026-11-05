from array import *
a= array('i', [2, 4, 5, 34, 7])
n=7
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i]+a[j]==n:
            print(a[i], a[j])