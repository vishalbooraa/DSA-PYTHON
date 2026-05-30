def find(idx,nums,dp,n):
    if idx>=n:
        return 0
    if dp[idx]!=-1:
        return dp[idx]
    rob=nums[idx]+find(idx+2,nums,dp,n)
    not_rob=find(idx+1,nums,dp,n)
    dp[idx]=max(rob,not_rob)
    return dp[idx]

def house_rob(nums):
    idx=0
    n=len(nums)
    dp=[-1]*n
    return find(idx,nums,dp,n)


print(house_rob([1,2,3,1]))
print(house_rob([2,7,9,3,1]))












# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 