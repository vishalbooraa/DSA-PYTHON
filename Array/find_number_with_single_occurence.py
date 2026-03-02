def number_single_occurence(arr):
    hash={}
    for i in arr:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    for i in hash:
        if hash[i]==1:
            return i


print(number_single_occurence([1, 2, 2, 4, 3, 1, 4]))
print(number_single_occurence([5]))



# Example 1

# Input : nums = [1, 2, 2, 4, 3, 1, 4]

# Output : 3

# Explanation : The integer 3 has appeared only once.

# Example 2

# Input : nums = [5]

# Output : 5

# Explanation : The integer 5 has appeared only once.