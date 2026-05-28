def check_sorted_or_rotated(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]>arr[(i+1)%len(arr)]:
            count+=1
    return count<=1




print(check_sorted_or_rotated([3,4,5,1,2]))
print(check_sorted_or_rotated([2,1,3,4]))
print(check_sorted_or_rotated([1,2,3]))



# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].
# Example 2:

# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.
# Example 3:

# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is the original sorted array.
# You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
 