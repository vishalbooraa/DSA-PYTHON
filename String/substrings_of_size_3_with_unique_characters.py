def total_substring(str):
    sub_strs=0
    for i in range(len(str)-2):
        if str[i]!=str[i+1] and str[i]!=str[i+2] and str[i+1]!=str[i+2]:
            sub_strs+=1
    return sub_strs

print(total_substring("xyzzaz"))
print(total_substring("aababcabc"))

    




# Example 1:

# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".
# Example 2:

# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".
 