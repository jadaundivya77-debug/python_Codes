n= 123312332
x=1
count=0
while n>0:
    d=n%10
    if x == d:
        count+=1
    n=n//10
print (count)