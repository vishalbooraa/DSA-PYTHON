def move(arr):
    start=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[start],arr[i]=arr[i],arr[start]
            start+=1
    return arr


print(move([0, 1, 4, 0, 5, 2]))
print(move([0, 0, 0, 1, 3, -2]))





# Input: nums = [0, 1, 4, 0, 5, 2]

# Output: [1, 4, 5, 2, 0, 0]

# Input: nums = [0, 0, 0, 1, 3, -2]

# Output: [1, 3, -2, 0, 0, 0]