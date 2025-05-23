def list_add(nums, total=[]):
    for num in nums:
        total.append(num)
        
    print(total)

nums = [1, 2, 3]
list_add(nums)


# Time complexity = O(n)
# Space complexity = O(n)