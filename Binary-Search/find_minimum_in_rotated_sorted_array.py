def find_minimum(arr):
    l=0
    r=len(arr)-1
    res=float("inf")
    while l<=r:
        mid=l+(r-l)//2
        if arr[l]<=arr[mid]:
            if arr[l]<res:
                res=arr[l]
            l=mid+1
        else:
            if arr[mid]<res:
                res=arr[mid]
            r=mid-1
    return res

print(find_minimum([4, 5, 6, 7, 0, 1, 2, 3]))
print(find_minimum([3, 4, 5, 1, 2]))
print(find_minimum([1, 2, 3, 4, 5]))      
print(find_minimum([2, 1])) 


# Example 1

# Input : nums = [4, 5, 6, 7, 0, 1, 2, 3]

# Output: 0

# Explanation: Here, the element 0 is the minimum element in the array.

# Example 2

# Input : nums = [3, 4, 5, 1, 2]

# Output: 1

# Explanation:Here, the element 1 is the minimum element in the array.