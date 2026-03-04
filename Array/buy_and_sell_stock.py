def stock_max_profit(arr):
    min_price=arr[0]
    max_profit=0
    for curr_price in arr:
        curr_profit=curr_price-min_price
        if curr_profit>max_profit:
            max_profit=curr_profit
        if curr_price<min_price:
            min_price=curr_price
    return max_profit


print(stock_max_profit([10, 7, 5, 8, 11, 9]))
print(stock_max_profit([5, 4, 3, 2, 1]))
    





# Example 1

# Input: arr = [10, 7, 5, 8, 11, 9]

# Output: 6

# Explanation: Buy on day 3 (price = 5) and sell on day 5 (price = 11), profit = 11 - 5 = 6.

# Example 2

# Input: arr = [5, 4, 3, 2, 1]

# Output: 0

# Explanation: In this case, no transactions are made. Therefore, the maximum profit remains 0.