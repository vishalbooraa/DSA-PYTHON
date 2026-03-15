def isomorphic_string(s,t):
    hash={}
    n=len(s)
    for i in range(n):
        if s[i] in hash:
            if hash[s[i]]!=t[i]:
                return False
        else:
            if t[i] in hash.values():
                return False
            hash[s[i]]=t[i]
    return True


print(isomorphic_string("ab","aa"))
print(isomorphic_string("egg","add"))
print(isomorphic_string("f11","b23"))
print(isomorphic_string("paper","title"))




# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "f11", t = "b23"

# Output: false

# Explanation:

# The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true