def find_subset(idx,arr,temp,res):
    res.append(temp[:])
    for i in range(idx,len(arr)):
        if i>idx and arr[i]==arr[i-1]:
            continue
        temp.append(arr[i])
        find_subset(i+1,arr,temp,res)
        temp.pop()


def subset(arr):
    arr.sort()
    res=[]
    temp=[]
    find_subset(0,arr,temp,res)
    return res

print(subset([1,2,2]))
print(subset([0]))




# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]