def remove_duplicates(arr):
    if len(arr)==0:
        return 0
    if len(arr)==1:
        return 1
    start=1
    for i in range(2,len(arr)):
        if arr[i]!=arr[start-1]:
            start+=1
            arr[start]=arr[i]
    return start+1

print(remove_duplicates([1,1,1,2,2,3]))
print(remove_duplicates([0,0,1,1,1,1,2,3,3]))
print(remove_duplicates([]))
print(remove_duplicates([1]))