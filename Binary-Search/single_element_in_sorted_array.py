def single_element(arr):
    if len(arr)==1:
        return arr[0]
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+(r-l)//2
        if mid==0 and arr[mid]!=arr[mid+1]:
            return arr[mid]
        if mid==len(arr)-1 and arr[mid]!=arr[mid-1]:
            return arr[mid]
        if arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]:
            return arr[mid]
        
        if mid%2==0:
            if arr[mid]==arr[mid-1]:
                r=mid-1
            else:
                l=mid+1
        else:
            if arr[mid]==arr[mid-1]:
                l=mid+1
            else:
                r=mid-1

print(single_element([1,1,2,3,3,4,4,8,8]))
print(single_element([3,3,7,7,10,11,11]))






# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10