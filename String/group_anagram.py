def sort_str(str):
    s_str=sorted(str)
    return "".join(s_str)

def group_anagram(strs):
    hash={}
    for str in strs:
        s_str=sort_str(str)
        if s_str in hash:
            hash[s_str].append(str)
        else:
            hash[s_str]=[str]
    res=[]

    for i in hash.values():
        res.append(i)
    return res


print(group_anagram(["eat","tea","tan","ate","nat","bat"]))
print(group_anagram([""]))
print(group_anagram(["a"]))






# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]