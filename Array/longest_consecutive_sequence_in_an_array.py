def longest_sequence(arr):
    max_count=0
    for i in arr:
        count=1
        while i+1 in arr:
            count+=1
            i+=1
        max_count=max(count,max_count)
    return max_count

print(longest_sequence([100, 4, 200, 1, 3, 2]))
print(longest_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))



# using set

def longest_sequence(arr):
    s = set(arr)
    max_len = 0

    for num in s:
        if num - 1 not in s:   # start of sequence
            curr = num
            count = 1

            while curr + 1 in s:
                curr += 1
                count += 1

            max_len = max(max_len, count)

    return max_len


print(longest_sequence([100, 4, 200, 1, 3, 2]))
print(longest_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))


# Example 1

# Input: nums = [100, 4, 200, 1, 3, 2]

# Output: 4

# Explanation:

# The longest sequence of consecutive elements in the array is [1, 2, 3, 4], which has a length of 4. This sequence can be formed regardless of the initial order of the elements in the array.

# Example 2

# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

# Output: 9

# Explanation:

# The longest sequence of consecutive elements in the array is [0, 1, 2, 3, 4, 5, 6, 7, 8], which has a length of 9. 