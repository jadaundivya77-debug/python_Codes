from array import array
nums= array("i", [1234, 745,7465,73464,234097,4444, 34643])
for i in range(len(nums)):
    min=i
    for j in range(i, len(nums)):
        if nums[min]> nums[j]:
            min=j
    nums[i], nums[min]=nums[min], nums[i]
print(nums)