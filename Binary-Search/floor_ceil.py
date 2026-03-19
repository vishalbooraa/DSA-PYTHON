def floor_ceil(arr,x):
    floor=-1
    ceil=-1
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]<=x:
            floor=arr[mid]
            l=mid+1
        else:
            r=mid-1
    
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]>=x:
            ceil=arr[mid]
            r=mid-1
        else:
            l=mid+1
    return floor,ceil


print(floor_ceil([3, 4, 4, 7, 8, 10],5))
print(floor_ceil([3, 4, 4, 7, 8, 10],8))



# Given a sorted array nums and an integer x. Find the floor and ceil of x in nums.
# The floor of x is the largest element in the array which is smaller than or equal to x.
# The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, output -1.

# # Example 1

# Input : nums =[3, 4, 4, 7, 8, 10], x= 5

# Output: 4 7

# Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.

# Example 2

# Input : nums =[3, 4, 4, 7, 8, 10], x= 8

# Output: 8 8

# Explanation: The floor of 8 in the array is 8, and the ceiling of 8 in the array is also 8.