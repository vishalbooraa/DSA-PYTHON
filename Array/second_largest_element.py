def second_largest_element(arr):
    first_largest=float("-inf")
    second_largest=float("-inf")
    for i in arr:
        if i >first_largest:
            second_largest=first_largest
            first_largest=i
        if i>second_largest:
            if i!=first_largest:
                second_largest=i
    return second_largest if second_largest != float("-inf") else -1




print(second_largest_element([8, 8, 7, 6, 5]))
print(second_largest_element([10, 10, 10, 10, 10]))
print(second_largest_element([7, 7, 2, 2, 10, 10, 10]))