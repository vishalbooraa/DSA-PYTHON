def find_ways(n,dp):
    if n<=3:
        return n
    if dp[n]!=-1:
        return dp[n]
    dp[n]=find_ways(n-1,dp)+find_ways(n-2,dp)
    return dp[n]


def climbing_chair(n):
    dp=[-1]*(n+1)
    return find_ways(n,dp)
    
print(climbing_chair(2))
print(climbing_chair(3))
print(climbing_chair(4))




# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step