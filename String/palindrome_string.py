def check_palindrome(str):
    l=0
    r=len(str)-1
    while l<r:
        if str[l]!=str[r]:
            return False
        l+=1
        r-=1
    return True


print(check_palindrome("aba"))
print(check_palindrome("abc"))
print(check_palindrome("xoxo"))
print(check_palindrome("DAD"))