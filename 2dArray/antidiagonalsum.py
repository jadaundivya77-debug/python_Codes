a=[[1,2,3], [4,5,6], [6,8,9]]
s=0
n=len(a)
for i in range(n):
    s+=a[i][n-1-i]
print(s)