'''list= [10, 20, 30, 40, 50]
i = 4

while i >= 0:
	print(list[i], end=" ")
	i -= 1'''

list=[1, 2, 3, 4, 5]
l=0
r=4
while(l< 2/len(list)):
	t=list[l]
	list[l]=list[r]
	list[r]=t
	l=l+1
	r=r-1
print(list)