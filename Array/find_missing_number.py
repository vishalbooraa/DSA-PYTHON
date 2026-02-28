def find_missing_number(arr):
    n=len(arr)
    sum=(n*(n+1))/2
    arr_sum=0
    for i in arr:
        arr_sum+=i
    return int(sum-arr_sum)

print(find_missing_number([0, 2, 3, 1, 4]))
print(find_missing_number([0, 1, 2, 4, 5, 6]))



# Example 1

# Input: nums = [0, 2, 3, 1, 4]

# Output: 5

# Explanation:

# nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]

# Example 2

# Input: nums = [0, 1, 2, 4, 5, 6]

# Output: 3

# Explanation:

# nums contains 0, 1, 2, 4, 5, 6 thus leaving 3 as the only missing number in the range [0, 6]