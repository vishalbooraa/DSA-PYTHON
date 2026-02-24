def remove_duplicates(arr):
    start=0
    for i in range(1,len(arr)):
        if arr[i]!=arr[start]:
            start+=1
            arr[start]=arr[i]
    return start+1



print(remove_duplicates([1,1,2]))
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))
