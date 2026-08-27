nums=[-1, 0, 1, 2, -1, -4]
ans=[]
answer=[]
for i in range(0, 6):

    for j in range(i,6):
        for k in range(j, 6):
            if (i==j or j==k or i==k):
                continue
            if ((nums[i]+ nums[j] + nums[k])==0):
                if (nums[i], nums[j], nums[k] not in ans):
                    ans.append([nums[i], nums[j], nums[k]])

print(answer)

            