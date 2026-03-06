def rearrange(arr):
    posIdx=0
    negIdx=1
    res=[0]*len(arr)
    for i in arr:
        if i>0:
            res[posIdx]=i
            posIdx+=2
        else:
            res[negIdx]=i
            negIdx+=2
    return res


print(rearrange([2, 4, 5, -1, -3, -4]))
print(rearrange([1, -1, -3, -4, 2, 3]))






# Example 1

# Input : nums = [2, 4, 5, -1, -3, -4]

# Output : [2, -1, 4, -3, 5, -4]

# Explanation:

# The positive number 2, 4, 5 maintain their relative positions and -1, -3, -4 maintain their relative positions

# Example 2

# Input : nums = [1, -1, -3, -4, 2, 3]

# Output : [1, -1, 2, -3, 3, -4]

# Explanation:

# The positive number 1, 2, 3 maintain their relative positions and -1, -3, -4 maintain their relative positions