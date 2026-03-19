def search(arr,tar):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]==tar:
            return mid
        elif arr[mid]<tar:
            l=mid+1
        else:
            r=mid-1
    return -1

print(search([-1,0,3,5,9,12],9))
print(search([-1,0,3,5,9,12],2))



# Example 1

# Input: nums = [-1,0,3,5,9,12], target = 9

# Output: 4

# Explanation: The target integer 9 exists in nums and its index is 4

# Example 2

# Input: nums = [-1,0,3,5,9,12], target = 2

# Output: -1

# Explanation: The target integer 2 does not exist in nums so return -1