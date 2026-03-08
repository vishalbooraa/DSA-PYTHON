def leaders(arr):
    res=[]
    res.append(arr[-1])
    largest=arr[-1]
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>largest:
            res.append(arr[i])
            largest=arr[i]
    return res[::-1]

print(leaders([1, 2, 5, 3, 1, 2]))
print(leaders([-3, 4, 5, 1, -4, -5]))




# Example 1

# Input: nums = [1, 2, 5, 3, 1, 2]

# Output: [5, 3, 2]

# Explanation:

# 2 is the rightmost element, 3 is the largest element in the index range [3, 5], 5 is the largest element in the index range [2, 5]

# Example 2

# Input: nums = [-3, 4, 5, 1, -4, -5]

# Output: [5, 1, -4, -5]

# Explanation:

# -5 is the rightmost element, -4 is the largest element in the index range [4, 5], 1 is the largest element in the index range [3, 5] and 5 is the largest element in the range [2, 5]