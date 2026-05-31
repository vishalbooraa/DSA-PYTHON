def find(day, last_task, points, dp):
    if day < 0:
        return 0

    if dp[day][last_task] != -1:
        return dp[day][last_task]

    max_points = float("-inf")

    for task in range(len(points[0])):
        if task != last_task:
            current_points = points[day][task] + find(day - 1, task, points, dp)
            max_points = max(max_points, current_points)

    dp[day][last_task] = max_points
    return dp[day][last_task]


def ninja_training(points):
    total_days = len(points)
    total_tasks = len(points[0])

    dp = [[-1] * (total_tasks + 1) for _ in range(total_days)]

    return find(total_days - 1, total_tasks, points, dp)


print(ninja_training([[10, 40, 70], [20, 50, 80], [30, 60, 90]]))
print(ninja_training([[70, 40, 10], [180, 20, 5], [200, 60, 30]]))
















# Example 1

# Input: matrix = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]

# Output: 210

# Explanation:

# Day 1: fighting practice = 70

# Day 2: stealth training = 50

# Day 3: fighting practice = 90

# Total = 70 + 50 + 90 = 210

# This gives the optimal points.

# Example 2

# Input: matrix = [[70, 40, 10], [180, 20, 5], [200, 60, 30]]

# Output: 290

# Explanation:

# Day 1: running = 70

# Day 2: stealth training = 20

# Day 3: running = 200

# Total = 70 + 20 + 200 = 290

# This gives the optimal points.