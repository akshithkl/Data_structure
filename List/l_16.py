def threeSumClosest(nums,target):
    result = 0
    for i in range(3):
        result += nums[i]
        if result > target:
            result -= 1
        if result < target:
            result += 1
                
    return result

nums = [-1,2,1,-4]
print(threeSumClosest(nums,2))