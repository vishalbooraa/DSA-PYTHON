def lower_bound(arr,x):
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

print(lower_bound([1,2,2,3],2))
print(lower_bound([3,5,8,15,19],9))




# Example 1

# Input : nums= [1,2,2,3], x = 2

# Output:1

# Explanation:

# Index 1 is the smallest index such that arr[1] >= x.

# Example 2

# Input : nums= [3,5,8,15,19], x = 9

# Output: 3

# Explanation:

# Index 3 is the smallest index such that arr[3] >= x.