def largest_odd_no(str):
    n=len(str)-1
    for i in range(n,-1,-1):
        if int(str[i])%2==1:
            return str[:i+1]
    return ""

print(largest_odd_no("52"))
print(largest_odd_no("4206"))
print(largest_odd_no("35427"))


# Example 1:

# Input: num = "52"
# Output: "5"
# Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
# Example 2:

# Input: num = "4206"
# Output: ""
# Explanation: There are no odd numbers in "4206".
# Example 3:

# Input: num = "35427"
# Output: "35427"
# Explanation: "35427" is already an odd number.