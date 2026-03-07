def next_permutation(arr):
    n=len(arr)
    pivot=-1
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            pivot=i
            break
    if pivot==-1:
        l=0
        r=n-1
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
        return arr
    for i in range(n-1,-1,-1):
        if arr[i]>arr[pivot]:
            arr[i],arr[pivot]=arr[pivot],arr[i]
            break
    l=pivot+1
    r=n-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr





print(next_permutation([1, 5, 8, 4, 7, 6, 5, 3, 1]))
print(next_permutation([1,2,3]))
print(next_permutation([3,2,1]))





# Example 1

# Input: nums = [1,2,3]

# Output: [1,3,2]

# Explanation:

# The next permutation of [1,2,3] is [1,3,2].

# Example 2

# Input: nums = [3,2,1]

# Output: [1,2,3]

# Explanation:

# [3,2,1] is the last permutation. So we return the first: [1,2,3].