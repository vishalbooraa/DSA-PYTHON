def merge(l,r,mid,arr):
    arr1=arr[l:mid+1]
    arr2=arr[mid+1:r+1]
    i=0
    j=0
    k=l
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            arr[k]=arr1[i]
            k+=1
            i+=1
        elif arr2[j]<arr1[i]:
            arr[k]=arr2[j]
            k+=1
            j+=1
    while i<len(arr1):
        arr[k]=arr1[i]
        i+=1
        k+=1
    while j<len(arr2):
        arr[k]=arr2[j]
        k+=1
        j+=1
    return arr

def divide(l,r,arr):
    if l>=r:
        return
    mid=(l+r)//2
    divide(l,mid,arr)
    divide(mid+1,r,arr)
    merge(l,r,mid,arr)
    


def merge_sort(arr):
    l=0
    r=len(arr)-1
    divide(l,r,arr)
    return arr


print(merge_sort([4,2,5,3,6,3,1,4,9]))