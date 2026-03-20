def count_occurrence(arr,x):
    l=0
    r=len(arr)-1
    first=-1
    last=-1
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
    
    if first==-1:
        return 0

    return (last+1)-first

print(count_occurrence([0, 0, 1, 1, 1, 2, 3],1))
print(count_occurrence([5, 5, 5, 5, 5, 5],5))
print(count_occurrence([5, 5, 5, 5, 5, 5],6))


# Example 1

# Input: arr = [0, 0, 1, 1, 1, 2, 3], target = 1

# Output: 3

# Explanation: The number 1 appears 3 times in the array.

# Example 2

# Input: arr = [5, 5, 5, 5, 5, 5], target = 5

# Output: 6

# Explanation: All elements in the array are 5, so the target appears 6 times.