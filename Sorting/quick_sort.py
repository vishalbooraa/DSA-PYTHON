def pivot(l,r,arr):
    piv=arr[r]
    start=l
    for i in range(l,r):
        if arr[i]<piv:
            arr[start],arr[i]=arr[i],arr[start]
            start+=1
    arr[start],arr[r]=arr[r],arr[start]
    return start


def divide(l,r,arr):
    if l>=r:
        return
    p=pivot(l,r,arr)
    divide(l,p-1,arr)
    divide(p+1,r,arr)

def quick_sort(arr):
    l=0
    r=len(arr)-1
    divide(l,r,arr)
    return arr

print(quick_sort([4,2,5,3,6,3,1,4,9]))
print(quick_sort([4,2,5,3]))