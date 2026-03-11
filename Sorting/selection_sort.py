def selection_sort(arr):
    for i in range(len(arr)):
        min=arr[i]
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[j]<min:
                min=arr[j]
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr

print(selection_sort([4,2,5,3,6,3,1,4,9]))