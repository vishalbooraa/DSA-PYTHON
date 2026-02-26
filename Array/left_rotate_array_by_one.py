def rotate(arr):
    l=1
    r=len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    l=0
    r=len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr

print(rotate( [1, 2, 3, 4, 5]))
print(rotate( [-1, 0, 3, 6]))






