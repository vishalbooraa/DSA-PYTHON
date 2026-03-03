def two_sum(arr,tar):
    hash={}
    n=len(arr)
    for i in range(n):
        comp=tar-arr[i]
        if comp in hash:
            return [hash[comp],i]
        hash[arr[i]]=i

print(two_sum([1, 6, 2, 10, 3],7))
print(two_sum([1, 3, 5, -7, 6, -3],0))






# Example 1

# Input: nums = [1, 6, 2, 10, 3], target = 7

# Output: [0, 1]

# Explanation:

# nums[0] + nums[1] = 1 + 6 = 7

# Example 2

# Input: nums = [1, 3, 5, -7, 6, -3], target = 0

# Output: [1, 5]

# Explanation:

# nums[1] + nums[5] = 3 + (-3) = 0