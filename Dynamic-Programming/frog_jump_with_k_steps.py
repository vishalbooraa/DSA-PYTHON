def find_min_energy(idx,height,k,dp):
    if idx==0:
        return 0
    min_energy=float("inf")
    if dp[idx]!=-1:
        return dp[idx]
    for i in range(1,k+1):
        if (idx-i)>=0:
            energy=abs(height[idx]-height[idx-i])+find_min_energy(idx-i,height,k,dp)
            min_energy=min(energy,min_energy)
    
    dp[idx]=min_energy
    
    return dp[idx]


def frog_jump(height,k):
    dp=[-1]*len(height)
    return find_min_energy(len(height)-1,height,k,dp)



print(frog_jump([10, 5, 20, 0, 15],2))
print(frog_jump([15, 4, 1, 14, 15],3))



# Example 1

# Input: heights = [10, 5, 20, 0, 15], k = 2

# Output: 15

# Explanation:

# 0th step -> 2nd step, cost = abs(10 - 20) = 10

# 2nd step -> 4th step, cost = abs(20 - 15) = 5

# Total cost = 10 + 5 = 15.

# Example 2

# Input: heights = [15, 4, 1, 14, 15], k = 3

# Output: 2

# Explanation:

# 0th step -> 3rd step, cost = abs(15 - 14) = 1

# 3rd step -> 4th step, cost = abs(14 - 15) = 1

# Total cost = 1 + 1 = 2.