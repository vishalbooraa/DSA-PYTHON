def longest_substring(str):
    i=0
    j=1
    res=1
    set1=set({})
    set1.add(str[i])

    while j<len(str):
        while str[j] in set1:
            set1.discard(str[i])
            i+=1
        set1.add(str[j])
        j+=1
        res=max(res,j-i)
    return res

print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))




# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.