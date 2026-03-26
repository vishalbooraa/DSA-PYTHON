def find_pow_set(idx,arr,track,res):
    if idx==len(arr):
        res.append(track[:])
        return
    track.append(arr[idx])
    find_pow_set(idx+1,arr,track,res)
    track.pop()
    find_pow_set(idx+1,arr,track,res)

def power_set(arr):
    res=[]
    track=[]
    find_pow_set(0,arr,track,res)
    return res

print(power_set([1,2,3]))


# Example 1

# Input : nums = [1, 2, 3]

# Output : [ [ ] , [1] , [2] , [1, 2] , [3] , [1, 3] , [2, 3] , [1, 2 ,3] ]

# Example 2

# Input : nums = [1, 2]

# Output : [ [ ] , [1] , [2] , [1,2] ]