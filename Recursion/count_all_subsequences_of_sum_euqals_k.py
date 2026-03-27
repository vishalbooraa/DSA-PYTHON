def subsequences(idx,arr,k):
    if idx==len(arr):
        if k==0:
            return 1
        return 0
    take=subsequences(idx+1,arr,k-arr[idx])
    not_take=subsequences(idx+1,arr,k)
    return take+not_take


def count_subsequences(arr,k):
    return subsequences(0,arr,k)

print(count_subsequences([4, 9, 2, 5, 1],10))
print(count_subsequences([4, 2, 10, 5, 1, 3],5))


# Example 1

# Input : nums = [4, 9, 2, 5, 1] , k = 10

# Output : 2

# Explanation : The possible subsets with sum k are [9, 1] , [4, 5, 1].

# Example 2

# Input : nums = [4, 2, 10, 5, 1, 3] , k = 5

# Output : 3

# Explanation : The possible subsets with sum k are [4, 1] , [2, 3] , [5].