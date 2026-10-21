L=[ 23, 56, 43, 45, 656, 7668, 8743, 4354, 6565 ]
count=0
for i in  range (1, len(L)-1):
    if L[i] > L[i-1] and L[i] > L[i+1]:
        count+=1
print(count)