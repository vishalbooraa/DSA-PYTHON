def remove_parenthesis(str):
    res=[]
    depth=0
    for i in str:
        if i=="(":
            if depth>0:
                res.append(i)
            depth+=1     
        else:
            depth-=1
            if depth>0:
                res.append(i)
            
    return "".join(res)

print(remove_parenthesis("(()())(())"))
print(remove_parenthesis("(()())(())(()(()))"))






# Example 1:

# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:

# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".