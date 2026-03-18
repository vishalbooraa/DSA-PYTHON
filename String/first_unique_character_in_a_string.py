def first_unique_char(str):
    freq={}
    for i in str:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    
    for i in range(len(str)):
        if freq[str[i]]==1:
            return i
    return -1

print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))

# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1