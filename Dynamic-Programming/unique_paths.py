def find(m,n,dp):
    if m==0 and n==0:
        return 1
    if m<0 or n<0:
        return 0
    
    if dp[m][n]!=-1:
        return dp[m][n]
    
    move_top=find(m-1,n,dp)
    move_left=find(m,n-1,dp)
    dp[m][n]=move_left+move_top
    return dp[m][n]


def unique_paths(m,n):
    dp=[[-1]*n for i in range(m)]
    return find(m-1,n-1,dp)


print(unique_paths(3,7))
print(unique_paths(3,2))







# Example 1:


# Input: m = 3, n = 7
# Output: 28


# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
 