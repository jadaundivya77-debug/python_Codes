from array import array
nums= array("i", [50, 20, 40, 30, 10])
n=len(nums)
for i in range(n-1):
    for j in range(n-1-i):
        if nums[j]>nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)