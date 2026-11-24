a=[1,0,1,0,1, 1,1,0,1,1,1,1,1,0]
def longest(a):
    count=0
    max_count=0
    for i in range(len(a)):
        if a[i]==1:
            count+=1
            if count>max_count:
                max_count=count
        else:
            count=0
    return max_count
print(longest(a))

s.start

   