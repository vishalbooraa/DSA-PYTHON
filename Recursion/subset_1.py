def find_subset(idx,arr,temp,res):
    if idx==len(arr):
        res.append(sum(temp))
        return
    temp.append(arr[idx])
    find_subset(idx+1,arr,temp,res)
    temp.pop()
    find_subset(idx+1,arr,temp,res)


def subset(arr):
    res=[]
    temp=[]
    find_subset(0,arr,temp,res)
    res.sort()
    return res


print(subset([2, 3]))
print(subset([5, 2, 1]))





# Example 1

# Input : nums = [2, 3]

# Output : [0, 2, 3, 5]

# Explanation :

# When no elements is taken then Sum = 0.

# When only 2 is taken then Sum = 2.

# When only 3 is taken then Sum = 3.

# When element 2 and 3 are taken then sum = 2+3 = 5.

# Example 2

# Input : nums = [5, 2, 1]

# Output : [0, 1, 2, 3, 5, 6, 7, 8]

# Explanation :

# When no elements is taken then Sum = 0.

# When only 5 is taken then Sum = 5.

# When only 2 is taken then Sum = 2.

# When only 1 is taken then Sum = 1.

# When element 2 and 1 are taken then sum = 2+1 = 3.