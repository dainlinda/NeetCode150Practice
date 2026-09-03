# Approach

## Check conditions to meet

- input: 
  - nums:list[int] / 1 to 100
    - nums[i]: the amount of money the ith house has / 0 to 100
      - the houses are arranged in a circle (e.g., the first house and the last house are neighbors)
      - ith house is the neighbor of the i-1th and i+1th house
  - cannot rob two adjacent houses  
- return: the max amount of money one can rob without alerting the police.

## Key idea

- Get each max amount of money for [0, i), (0,i], and get max of both of them. 

1. define subproblem in words
- Let 
  - R[i][0] = the max amount of money from house 0th to (i-1)th
  - R[i][1] = the max amount of money from house 1st to ith

1. state recursive relation
- base
  - R[1] = [nums[0], nums[1]]
    - R[1][0] starts from index 0, R[1][1] starts from index 1
  - R[2] = [max(nums[0], nums[1]), max(nums[1], nums[2])] 
- Recursive relation:
  - R[i][0] = max(R[i - 1][0], R[i - 2][0] + nums[i - 1])
    - num added to R[i-2][0] should be i-1 because it does not include ith
  - R[i][1] = max(R[i - 1][1], R[i - 2][1] + nums[i])


## Complexity
- time: O(n) because for-loop iteration dominates
- space: O(2*n) for table R, therefore O(n)
 
## Caveat and Reflection (Claude-assisted)
- Space can be optimized from O(n) to O(1) by keeping only the last two rows of R (rolling variables) instead of the full table, since each step only depends on R[i-1] and R[i-2].
