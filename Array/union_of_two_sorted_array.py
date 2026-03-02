def union(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    i=0
    j=0
    un=[]
    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            if len(un)==0 or un[-1]!=arr1[i]:
                un.append(arr1[i])
            i+=1
        elif arr2[j]<arr1[i]:
            if len(un)==0 or un[-1]!=arr2[j]:
                un.append(arr2[j])
            j+=1
        else:
            if len(un)==0 or un[-1]!=arr1[i]:
                un.append(arr1[i])
            i+=1
            j+=1
    
    while i<n1:
        if len(un)==0 or un[-1]!=arr1[i]:
            un.append(arr1[i])
        i+=1
    while j<n2:
        if len(un)==0 or un[-1]!=arr2[j]:
            un.append(arr2[j])
        j+=1

    return un

print(union([1, 2, 3, 4, 5],[1, 2, 7]))
print(union([3, 4, 6, 7, 9, 9],[1, 5, 7, 8, 8]))



# Example 1

# Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]

# Output: [1, 2, 3, 4, 5, 7]

# Explanation:

# The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

# Example 2

# Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]

# Output: [1, 3, 4, 5, 6, 7, 8, 9]

# Explanation:

# The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2