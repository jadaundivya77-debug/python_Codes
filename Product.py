nums= [1,2,3,4]
ans=[]

for i in range(0, 4):
    product=1
    for j in range(0, 4):
        if j==i:
            continue
        product = product*nums[j]
    ans.append(product)
print(ans)


