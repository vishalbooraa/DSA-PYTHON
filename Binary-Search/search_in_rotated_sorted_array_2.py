def search_in_rotated_array(arr,k):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]==k:
            return True
        elif arr[l]==arr[mid]==arr[r]:
            l+=1
            r-=1
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
    return False

print(search_in_rotated_array([2,5,6,0,0,1,2],2))
print(search_in_rotated_array([2,5,6,0,0,1,2],3))
print(search_in_rotated_array([2,2,2,2,2],2))
    


# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false