def peak_element(arr):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+(r-l)//2
        left=arr[mid-1] if mid>0 else float("-inf")
        right=arr[mid+1] if mid<len(arr)-1 else float("-inf")
        if left<arr[mid] and arr[mid]>right:
            return mid
        if arr[mid]<right:
            l=mid+1
        else:
            r=mid-1

print(peak_element([1, 2, 3, 4, 5, 6, 7, 8, 5, 1]))
print(peak_element([1, 2, 1, 3, 5, 6, 4]))

def peak_element(arr):
    l, r = 0, len(arr) - 1

    while l < r:
        mid = (l + r) // 2

        if arr[mid] < arr[mid + 1]:
            l = mid + 1
        else:
            r = mid

    return l

print(peak_element([1, 2, 3, 4, 5, 6, 7, 8, 5, 1]))
print(peak_element([1, 2, 1, 3, 5, 6, 4]))


# Example 1

# Input : arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]

# Output: 7

# Explanation: In this example, there is only 1 peak that is at index 7.

# Example 2

# Input : arr = [1, 2, 1, 3, 5, 6, 4]

# Output: 1

# Explanation: In this example, there are 2 peak numbers at indices 1 and 5. We can consider any of them.