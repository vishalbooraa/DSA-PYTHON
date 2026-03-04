def sort(arr):
    maxi=max(arr)
    freq=[0]*(maxi+1)
    for i in arr:
        freq[i]+=1
    start=0
    for j in range(len(freq)):
        while freq[j]>0:
            arr[start]=j
            start+=1
            freq[j]-=1
    return arr


print(sort([1, 0, 2, 1, 0]))
print(sort([0, 0, 1, 1, 1]))



# Example 1

# Input: nums = [1, 0, 2, 1, 0]

# Output: [0, 0, 1, 1, 2]

# Explanation:

# The nums array in sorted order has 2 zeroes, 2 ones and 1 two

# Example 2

# Input: nums = [0, 0, 1, 1, 1]

# Output: [0, 0, 1, 1, 1]

# Explanation:

# The nums array in sorted order has 2 zeroes, 3 ones and zero twos