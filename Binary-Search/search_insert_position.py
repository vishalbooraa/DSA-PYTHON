def insert_position(arr,x):
    l=0
    r=len(arr)-1
    res=len(arr)
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]>=x:
            res=mid
            r=mid-1
        else:
            l=mid+1
    return res

print(insert_position([1, 3, 5, 6],5))
print(insert_position([1, 3, 5, 6],2))




# Example 1

# Input: nums = [1, 3, 5, 6], target = 5

# Output: 2

# Explanation: The target value 5 is found at index 2 in the sorted array. Hence, the function returns 2.

# Example 2

# Input: nums = [1, 3, 5, 6], target = 2

# Output: 1

# Explanation: The target value 2 is not found in the array. However, it should be inserted at index 1 to maintain the sorted order of the array.