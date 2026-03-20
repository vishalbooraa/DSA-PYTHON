def search_rotated_array(arr,k):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]==k:
            return mid
        elif arr[l]<=arr[mid]:
            if arr[l]<=k and k<arr[mid]:
                r=mid-1
            else:
                l=mid+1
        else:
            if arr[mid]<k and k<=arr[r]:
                l=mid+1
            else:
                r=mid-1
    return -1

print(search_rotated_array([4, 5, 6, 7, 0, 1, 2],0))
print(search_rotated_array([4, 5, 6, 7, 0, 1, 2],3))




# Example 1

# Input : nums = [4, 5, 6, 7, 0, 1, 2], k = 0

# Output: 4

# Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

# Example 2

# Input: nums = [4, 5, 6, 7, 0, 1, 2], k = 3

# Output: -1

# Explanation: Here, the target is 3. Since 3 is not present in the given rotated sorted array. Thus, we get the output as -1.