def search(arr,tar):
    for i in range(len(arr)):
        if arr[i]==tar:
            return i
    return -1

print(search([2, 3, 4, 5, 3],3))
print(search([2, -4, 4, 0, 10],6))






# Example 1

# Input: nums = [2, 3, 4, 5, 3], target = 3

# Output: 1

# Explanation:

# The first occurence of 3 in nums is at index 1

# Example 2

# Input: nums = [2, -4, 4, 0, 10], target = 6

# Output: -1

# Explanation:

# The value 6 does not occur in the array, hence output is -1