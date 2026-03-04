def majority_element(arr):
    hash={}
    for i in arr:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    major=len(arr)//2
    for i in hash:
        if hash[i]>major:
            return i
    

print(majority_element([7, 0, 0, 1, 7, 7, 2, 7, 7]))
print(majority_element([1, 1, 1, 2, 1, 2]))


# Example 1

# Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

# Output: 7

# Explanation:

# The number 7 appears 5 times in the 9 sized array

# Example 2

# Input: nums = [1, 1, 1, 2, 1, 2]

# Output: 1

# Explanation:

# The number 1 appears 4 times in the 6 sized array