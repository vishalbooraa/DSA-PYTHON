def longest_subarray_with_sum_k(arr,k):
    hash={}
    sum=0
    n=len(arr)
    longest_subarray=0
    for i in range(n):
        sum+=arr[i]
        if sum==k:
            longest_subarray=i+1
        rem=sum-k
        if rem in hash:
            nl=i-hash[rem]
            longest_subarray=max(nl,longest_subarray)
        if sum not in hash:
            hash[sum]=i
    return longest_subarray

print(longest_subarray_with_sum_k([10, 5, 2, 7, 1, 9],15))
print(longest_subarray_with_sum_k([-3, 2, 1],6))

# Example 1

# Input: nums = [10, 5, 2, 7, 1, 9],  k=15

# Output: 4

# Explanation:

# The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

# Example 2

# Input: nums = [-3, 2, 1], k=6

# Output: 0

# Explanation:

# There is no sub-array in the array that sums to 6. Therefore, the output is 0.