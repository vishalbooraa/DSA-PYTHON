def find(m,n,grid,dp):
    if m<0 or n<0:
        return 0
    if grid[m][n]==1:
        return 0
    if m==0 and n==0:
        return 1
    if dp[m][n]!=-1:
        return dp[m][n]
    move_top=find(m-1,n,grid,dp)
    move_left=find(m,n-1,grid,dp)
    dp[m][n]=move_top+move_left
    return dp[m][n]


def unique_paths(grid):
    m=len(grid)
    n=len(grid[0])
    dp=[[-1]*n for i in range(m)]
    return find(m-1,n-1,grid,dp)


print(unique_paths([[0,0,0],[0,1,0],[0,0,0]]))
print(unique_paths([[0,1],[0,0]]))





# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right


# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1