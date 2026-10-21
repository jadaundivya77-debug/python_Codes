#Insertion sort 
from array import array
num= array("i", [10, 40, 50, 30, 20])
for i in range (1, len(num)):
    key=num[i]
    j=i-1
    while j>=0 and num[j] > key:
        num[j+1]=num[j]
        j-=1
    num[j+1]=key
print(num)