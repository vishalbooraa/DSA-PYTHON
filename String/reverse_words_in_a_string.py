def reverse_words(str):
    words=[]
    n=len(str)
    i=0
    
    while i<n:
        while i<n and str[i]==" ":
            i+=1
        word=''
        while i<n and str[i]!=" ":
            word+=str[i]
            i+=1
        if word:
            words.append(word)

    l=0
    r=len(words)-1
    while l<r:
        words[l],words[r]=words[r],words[l]
        l+=1
        r-=1
    return " ".join(words)


print(reverse_words("the sky is blue"))
print(reverse_words("  hello world  "))
print(reverse_words("a good   example"))






# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.