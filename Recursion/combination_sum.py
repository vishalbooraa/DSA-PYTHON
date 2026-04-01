def find_combinations(idx,cand,tar,track,res):
    if tar==0:
        res.append(track[:])
        return
    if idx==len(cand) or tar<0:
        return
    track.append(cand[idx])
    find_combinations(idx,cand,tar-cand[idx],track,res)
    track.pop()
    find_combinations(idx+1,cand,tar,track,res)

def combination_sum(cand,tar):
    res=[]
    track=[]
    find_combinations(0,cand,tar,track,res)
    return res


print(combination_sum([2,3,6,7],7))


# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []