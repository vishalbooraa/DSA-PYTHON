def find(r,pc,matrix,dp):
    if r<0:
        return 0
    if dp[r][pc]!=-1:
        return dp[r][pc]
    maxm=float("-inf")
    for i in range(len(matrix[0])):
        if i!=pc:
            curr=matrix[r][i]+find(r-1,i,matrix,dp)
            maxm=max(maxm,curr)
    dp[r][pc]=maxm
    return dp[r][pc]



def ninja_training(matrix):
    n=len(matrix)
    col=len(matrix[0])
    dp=[[-1]*(col+1) for i in range(n)]
    return find(n-1,col,matrix,dp)




print(ninja_training([[10, 40, 70], [20, 50, 80], [30, 60, 90]]))
print(ninja_training([[70, 40, 10], [180, 20, 5], [200, 60, 30]]))
















# Example 1

# Input: matrix = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]

# Output: 210

# Explanation:

# Day 1: fighting practice = 70

# Day 2: stealth training = 50

# Day 3: fighting practice = 90

# Total = 70 + 50 + 90 = 210

# This gives the optimal points.

# Example 2

# Input: matrix = [[70, 40, 10], [180, 20, 5], [200, 60, 30]]

# Output: 290

# Explanation:

# Day 1: running = 70

# Day 2: stealth training = 20

# Day 3: running = 200

# Total = 70 + 20 + 200 = 290

# This gives the optimal points.