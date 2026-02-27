def rotate(arr,k):
    n=len(arr)
    k=k%n
    l=0
    r=k-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    l=k
    r=n-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    l=0
    r=n-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr


print(rotate([1, 2, 3, 4, 5, 6],2))
print(rotate([3, 4, 1, 5, 3, -5],8))







# Input: nums = [1, 2, 3, 4, 5, 6], k = 2

# Output: nums = [3, 4, 5, 6, 1, 2]

# Input: nums = [3, 4, 1, 5, 3, -5], k = 8

# Output: nums = [1, 5, 3, -5, 3, 4]