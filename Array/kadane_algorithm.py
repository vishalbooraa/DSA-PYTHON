def kadane_algorithm(arr):
    max_sum=float("-inf")
    curr_sum=0
    for i in arr:
        curr_sum+=i
        if curr_sum>max_sum:
            max_sum=curr_sum
        if curr_sum<0:
            curr_sum=0
    return max_sum

print(kadane_algorithm([2, 3, 5, -2, 7, -4]))
print(kadane_algorithm([-2, -3, -7, -2, -10, -4]))



# Example 1

# Input: nums = [2, 3, 5, -2, 7, -4]

# Output: 15

# Explanation:

# The subarray from index 0 to index 4 has the largest sum = 15

# Example 2

# Input: nums = [-2, -3, -7, -2, -10, -4]

# Output: -2

# Explanation:

# The element on index 0 or index 3 make up the largest sum when taken as a subarray