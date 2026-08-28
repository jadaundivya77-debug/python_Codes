nums=[-1, 0, 1, 2, -1, -4]
ans=[]

for i in range(0, 6):
     for j in range(i+1,6):
        for k in range(j+1, 6):
            
            if (nums[i]+ nums[j] + nums[k]==0):
                triplet= [nums[i], nums[j], nums[k]]
                triplet.sort()
                if triplet not in ans:
                    ans.append(triplet)

print(ans)

            