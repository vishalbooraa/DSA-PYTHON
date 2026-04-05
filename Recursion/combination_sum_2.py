def find_combinations(idx,cand,tar,temp,res):
    if tar==0:
        res.append(temp[:])
        return
    if idx==len(cand):
        return
    
    for i in range(idx,len(cand)):
        if i>idx and cand[i]==cand[i-1]:
            continue
        temp.append(cand[i])
        find_combinations(i+1,cand,tar-cand[i],temp,res)
        temp.pop()


def combination_sum(cand,tar):
    cand.sort()
    temp=[]
    res=[]
    find_combinations(0,cand,tar,temp,res)
    return res


print(combination_sum([10,1,2,7,6,1,5],8))



# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]