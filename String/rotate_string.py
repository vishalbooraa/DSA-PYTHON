def rotate_string(str,goal):
    if goal in str + str:
        return True
    return False

print(rotate_string("abcde","cdeab"))
print(rotate_string("abcde","abced"))


# Example 1:

# Input: str = "abcde", goal = "cdeab"
# Output: true
# Example 2:

# Input: str = "abcde", goal = "abced"
# Output: false