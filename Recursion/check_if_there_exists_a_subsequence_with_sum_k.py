def check_subsequence_existence(idx,arr,curr_sum,k):
    if idx==len(arr):
        if curr_sum==k:
            return True
        return False

    take=check_subsequence_existence(idx+1,arr,curr_sum+arr[idx],k)
    not_take=check_subsequence_existence(idx+1,arr,curr_sum,k)
    return take or not_take


def subsequence_with_sum_k(arr,k):
    return check_subsequence_existence(0,arr,0,k)
    
print(subsequence_with_sum_k([1, 2, 3, 4, 5],8))
print(subsequence_with_sum_k([4, 3, 9, 2],10))


# Example 1

# Input : nums = [1, 2, 3, 4, 5] , k = 8

# Output : Yes

# Explanation : The subsequences like [1, 2, 5] , [1, 3, 4] , [3, 5] sum up to 8.

# Example 2

# Input : nums = [4, 3, 9, 2] , k = 10

# Output : No

# Explanation : No subsequence can sum up to 10.