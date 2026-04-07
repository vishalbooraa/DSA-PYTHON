def find_number(n,dp):
    if n<=0:
        return 0
    if n==1:
        return 1
    if dp[n]!=-1:
        return dp[n]
    dp[n]=find_number(n-1,dp)+find_number(n-2,dp)
    return dp[n]

def fibonacci_number(n):
    dp=[-1]*(n+1)
    return find_number(n,dp)


print(fibonacci_number(5))
print(fibonacci_number(6))