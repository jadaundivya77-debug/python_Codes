A=[10, 20, 30, 10, 20, 40, 30]
d={}
for i in A:
    count=1
    if i not in d:
        d[i]=count
    else:
        count+=1
    d[i]=count
print(d)
        
 


