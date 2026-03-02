def max_consecutive_ones(arr):
    n=len(arr)
    i=0
    max_ones=0
    while i<n:
        count=0
        if arr[i]==1:
            while i<n and arr[i]==1:
                count+=1
                i+=1
        max_ones=max(count,max_ones)
        i+=1
    return max_ones

print(max_consecutive_ones([1, 1, 0, 0, 1, 1, 1, 0]))
print(max_consecutive_ones([0, 0, 0, 0, 0, 0, 0, 0]))

# using for loop

def max_consecutive_ones(arr):
    max_ones = 0
    count = 0

    for num in arr:
        if num == 1:
            count += 1
            max_ones = max(max_ones, count)
        else:
            count = 0

    return max_ones

print(max_consecutive_ones([1, 1, 0, 0, 1, 1, 1, 0]))
print(max_consecutive_ones([0, 0, 0, 0, 0, 0, 0, 0]))

# Example 1

# Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]

# Output: 3

# Explanation:

# The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s

# Example 2

# Input: nums = [0, 0, 0, 0, 0, 0, 0, 0]

# Output: 0

# Explanation:

# No 1s are present in nums, thus we return 0