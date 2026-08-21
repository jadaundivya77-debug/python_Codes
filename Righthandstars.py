'''for i in range(1,6):
    for k in range(i-1):
        print(" ", end=" ")
    for j in range(i,6):
        print("*", end=" ")
    print()'''

list=[1, 2, 3, 4, 5]
l=0
r=4
while[l< 2/len(list)]:
	t=list[l]
	list[l]=list[r]
	list[r]=t
	l=l+1
	r=r-1
print(list)