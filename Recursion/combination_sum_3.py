def find_combinations(idx,k,n,temp,res):
    if len(temp)==k and n==0:
        res.append(temp[:])
        return
    if len(temp)==k and n!=0:
        return
    if idx==10:
        return 
    temp.append(idx)
    find_combinations(idx+1,k,n-idx,temp,res)
    temp.pop()
    find_combinations(idx+1,k,n,temp,res)

def combination_sum(k,n):
    temp=[]
    res=[]
    find_combinations(1,k,n,temp,res)
    return res

print(combination_sum(3,7))
print(combination_sum(3,9))
print(combination_sum(4,1))





# Example 1:

# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# Example 2:

# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
# Example 3:

# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.