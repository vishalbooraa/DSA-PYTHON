def check_sorted(arr):
    asc=True
    desc=True
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            desc=False
        if arr[i]>arr[i+1]:
            asc=False
        if not asc and not desc:
            return False
    return asc or desc

print(check_sorted([1, 2, 3, 4, 5]))
print(check_sorted([5,4,3,2,1]))
print(check_sorted( [1, 2, 1, 4, 5]))