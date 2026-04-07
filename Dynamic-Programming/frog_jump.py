def find_energy(idx,height,dp):
    if idx==0:
        return 0
    if dp[idx]!=-1:
        return dp[idx]
    jump1=abs(height[idx]-height[idx-1])+find_energy(idx-1,height,dp)
    jump2=float("inf")
    if idx>1:
        jump2=abs(height[idx]-height[idx-2])+find_energy(idx-2,height,dp)
    dp[idx]=min(jump1,jump2)
    return dp[idx]
        


def frog_jump(height):
    dp=[-1]*len(height)
    return find_energy(len(height)-1,height,dp)


print(frog_jump([2, 1, 3, 5, 4]))
print(frog_jump([7, 5, 1, 2, 6]))
    



# Example 1

# Input: heights = [2, 1, 3, 5, 4]

# Output: 2

# Explanation:

# One possible route can be,

# 0th step -> 2nd Step = abs(2 - 3) = 1

# 2nd step -> 4th step = abs(3 - 4) = 1

# Total = 1 + 1 = 2.

# Example 2

# Input: heights = [7, 5, 1, 2, 6]

# Output: 9

# Explanation:

# One possible route can be,

# 0th step -> 1st Step = abs(7 - 5) = 2

# 1st step -> 3rd step = abs(5 - 2) = 3

# 3rd step -> 4th step = abs(2 - 6) = 4

# Total = 2 + 3 + 4 = 9.