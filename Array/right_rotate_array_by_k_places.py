def rotate(arr,k):
    if len(arr)==0:
        return arr
    l=0
    r=len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    k=k%len(arr)
    l=0
    r=k-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    l=k
    r=len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr



print(rotate([1,2,3,4,5,6,7],3))
print(rotate([1, 2, 3, 4, 5, 6],2))
print(rotate([],2))
