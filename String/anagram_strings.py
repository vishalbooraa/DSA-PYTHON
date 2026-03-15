def anagram_strings(s,t):
    hash={}
    for i in s:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    
    for i in t:
        if i in hash:
            hash[i]-=1
        else:
            return False
        
    for i in hash:
        if hash[i]!=0:
            return False
    return True


print(anagram_strings("anagram","nagaram"))
print(anagram_strings("rat","car"))
    





# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false