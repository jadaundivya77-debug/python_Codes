a=[[1,2,3], [4,5,6], [6,8,9]]
s=0
n=len(a)
for i in range(n):
    s+=a[i][n-1-i]
print(s)


i=0
j=len(a)-1
for k in range (len(a)):
    s+=a[i][j]
    i+=1
    j-=1
