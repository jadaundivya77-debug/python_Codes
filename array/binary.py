#Binary search is a searching algorithm used to find the position of a specific element in a sorted array. It works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.
#it si used for sorted arrays only
#the number we have to find id called key.
#there are 3 sections, mid, left and right. mid is the middle element of the array, left is the first element of the array 
# and right is the last element of the array.
# 2 pointers low and high are used to keep track of the left and right sections of the array. low is initialized to 0 and
#  high is initialized to the length of the array - 1. The mid pointer is calculated as (low + high) // 
# 2. If the key is equal to the mid element, the search is successful. If the key is less than the mid element,
#  the search continues in the left section by updating high to mid - 1. If the key is greater than the mid element,
#  the search continues in the right section by updating low to mid + 1. This process continues until the key is found
#  or low becomes greater than high, indicating that the key is not present in the array.
from array import array
numbers = array('i', [10, 20, 30, 40, 50])
key=25
low=0
high= len(numbers)-1
while low <= high:
    mid = (low + high)//2
    if numbers[mid]==key:
        print("Element is found")
        break
    elif key<numbers[mid]:
        high= mid-1
    else:
        low= mid+1
else:
    print("Element is not found")