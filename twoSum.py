def twoSum(nums, target):
    res = []
    found = False
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j != i:
                if target - nums[i] == nums[j]:
                    res.append(i)
                    res.append(j)
                    return res

print(twoSum([1, 3, 2, 10, 2], 5))
print(twoSum([1, 3, 2, 10, 2], 3))
print(twoSum([1, 3, 2, 10, 2], 4))