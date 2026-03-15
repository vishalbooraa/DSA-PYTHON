def sort_characters(str):
    hash={}
    for i in str:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    
    dict1= dict(sorted(hash.items(), key= lambda x:x[1], reverse=True))

    res=""
    for char,freq in dict1.items():
        res+=char*freq
    return res


print(sort_characters("tree"))
print(sort_characters("cccaaa"))
print(sort_characters("Aabb"))





# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.