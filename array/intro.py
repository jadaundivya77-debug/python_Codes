#an array is container which can hold a fix number of items and thesse are same datatype
#import array (module)
from array import array
numbers= array('i', [2, 4, 5,6])
#value
for i in numbers:
    print(i)
print(numbers[1]) # use index to access the elements of array

#index
for i in range(len(numbers)):
    print(numbers[i])
#type code "b" : signed byte fro pawsitive and negative byte, "B" fro unsigned byte (only pawsitive),
#  "i": signed integer, "I": insigned integer,

#add element to array using append() method
numbers.append(7)
for i in numbers:
    print(i)

#extend() method is used to add multiple elements to the array
numbers.extend([8,9,10])
for i in numbers:
    print(i)


a=array('i', [1,2,3,4])
b=array('i', [5,6,7,8])
a.extend(b)
print(a)


#insert() method is used to insert an element at a specific index in the array
numbers.insert(3, 60)  #3 is index value 60 is inserted at index 3
for i in numbers:
    print(i)


#remove() method is used to remove the first occurrence of a specific element from the array
numbers.remove (6)  #you have to guve the vallue of the element you want to remove


#pop() method is used to remove an element from the array at a specific index
numbers.pop(3)  # removes the element at index 3
value = numbers.pop()   #removes the last element from the array
print("Removed value is: ", value)


#index() method is used to find the index of the first occurrence of a specific element in the array
'''index = numbers.index(60)
print("Index of 60 is: ", index)'''

#COUNT() method is used to count the number of occurrences of a specific element in the array
'''count = numbers.count(4)
print("Count of 4 is: ", count)'''


#reverse() method is used to reverse the order of elements in the array
'''numbers.reverse()
print("Reversed array is: ", numbers)'''

#itemsize() method is used to get the size of each element in the array in bytes
n=array('i', [1,2,3,4])
print(n.itemsize)  # size of each element in bytes

#slicing is used to access a range of elements in the array
sliced_array = numbers[1:4]  #access elements from index 1 to 3 (4 is not included)
print("Sliced array is: ", sliced_array)
#[:4] - access elements from the beginning up to index 3
#[1:4] - access elements from index 1 to 3
#[1:4:2] - access elements from index 1 to 3 with a step of 2

#copy() method is used to create a copy of the array

'''copied_array = numbers.copy()
print("Copied array is: ", copied_array)

new_arr = array('i', numbers)  # create a new array with the same type code and elements as the original array
print("New array is: ", new_arr)

#covert array to list using tolist() method
list_from_array = numbers.tolist()

# covert list to array using fromlist() method
new_array_from_list = array('i', list_from_array)'''

#input from user to create an array
arr=array('i')
n=int(input("Enter the number of elements: "))
for i in range(n):
    value=int(input("Enter the value: "))
    arr.append(value)
print("Array created is: ", arr)