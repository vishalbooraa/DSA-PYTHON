def first_and_last_occurence(arr,x):
    first=-1
    last=-1
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]==x:
            first=mid
            r=mid-1
        elif arr[mid]>x:
            r=mid-1
        else:
            l=mid+1
    
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]==x:
            last=mid
            l=mid+1
        elif arr[mid]<x:
            l=mid+1
        else:
            r=mid-1
    
    return [first,last]

print(first_and_last_occurence([5, 7, 7, 8, 8, 10],8))
print(first_and_last_occurence([5, 7, 7, 8, 8, 10],6))


# Example 1

# Input: nums = [5, 7, 7, 8, 8, 10], target = 8

# Output: [3, 4]

# Explanation:The target is 8, and it appears in the array at indices 3 and 4, so the output is [3,4]

# Example 2

# Input: nums = [5, 7, 7, 8, 8, 10], target = 6

# Output: [-1, -1]

# Expalantion: The target is 6, which is not present in the array. Therefore, the output is [-1, -1].