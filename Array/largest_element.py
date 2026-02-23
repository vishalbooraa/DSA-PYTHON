def largest_element(arr):
    largest=float("-inf")
    for i in arr:
        if i>largest:
            largest=i
    return largest

print(largest_element([3, 3, 6, 1]))
print(largest_element([3, 3, 0, 99, -40]))
print(largest_element( [-4, -3, 0, 1, -8]))