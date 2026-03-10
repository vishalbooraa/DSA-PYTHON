def bubble_sort(arr):
    for i in range(len(arr)):
        swap=False
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
        if not swap:
            return arr
    return arr

print(bubble_sort([4,2,5,3,6,3,1,4,9]))