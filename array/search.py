from array import *
numbers = array('i', [10, 20, 30, 40, 50])
no = 30
a=0
'''for  i in range(len(numbers)):
    if numbers[i]==no:
        print("Element is found")
        a=1
        break
if a==0:
    print("Element is not found")'''


if no in numbers:
    print("found")
else:
    print("no")