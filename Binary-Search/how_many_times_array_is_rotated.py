def times_rotated(arr):
    l=0
    r=len(arr)-1
    total_rotation=0
    min=float("inf")
    while l<=r:
        mid=l+(r-l)//2
        if arr[l]<=arr[mid]:
            if arr[l]<min:
                min=arr[l]
                total_rotation=l
            l=mid+1
        else:
            if arr[mid]<min:
                total_rotation=mid
            r=mid-1
    return total_rotation

print(times_rotated([4, 5, 6, 7, 0, 1, 2, 3]))
print(times_rotated([3, 4, 5, 1, 2]))
print(times_rotated([1,2,3,4,5,6]))


# Example 1

# Input : nums = [4, 5, 6, 7, 0, 1, 2, 3]

# Output: 4

# Explanation: The original array should be [0, 1, 2, 3, 4, 5, 6, 7]. So, we can notice that the array has been rotated 4 times.

# Example 2

# Input: nums = [3, 4, 5, 1, 2]

# Output: 3

# Explanation: The original array should be [1, 2, 3, 4, 5]. So, we can notice that the array has been rotated 3 times.