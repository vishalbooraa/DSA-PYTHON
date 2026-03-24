def find_pow(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    half=find_pow(x,n//2)
    if n%2==0:
        return half*half
    return half*half*x

def pow(x,n):
    if n<0:
        return 1/find_pow(x,-n)
    return find_pow(x,n)

print(pow(2,10))
print(pow(2,-2))


# Example 1

# Input : x = 2.0000 , n = 10

# Output : 1024.0000

# Explanation : Answer = 2^10 => 1024.

# Example 2

# Input : x = 2.0000 , n = -2

# Output : 0.2500

# Explanation : Answer = 2^(-2) = 1/4 => 0.25.