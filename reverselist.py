'''list= [10, 20, 30, 40, 50]
i = 4

while i >= 0:
	print(list[i], end=" ")
	i -= 1'''


#Swapping the indexes
list=[1, 2, 3, 4, 5]
l=0
r=4
while(l< len(list)/2):
	#t=list[l]
	#list[l]=list[r]
	#list[r]=t
	list[l], list[r]= list[r], list[l]
	l=l+1
	r=r-1
print(list)