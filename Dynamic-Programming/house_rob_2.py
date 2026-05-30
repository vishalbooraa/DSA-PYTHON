def find(idx,arr,dp):
    if idx>=len(arr):
        return 0
    if dp[idx]!=-1:
        return dp[idx]
    rob=arr[idx]+find(idx+2,arr,dp)
    not_rob=find(idx+1,arr,dp)
    dp[idx]=max(rob,not_rob)
    return dp[idx]


def house_rob(arr):
    n=len(arr)
    if n==1:
        return arr[0]
    dp1=[-1]*(n-1)
    dp2=[-1]*(n-1)
    arr1=arr[:n-1]
    arr2=arr[1:n]
    case1=find(0,arr1,dp1)
    case2=find(0,arr2,dp2)
    return max(case1,case2)


print(house_rob([2,3,2]))
print(house_rob([1,2,3,1]))
print(house_rob([1,2,3]))


# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:

# Input: nums = [1,2,3]
# Output: 3