# Approach

## Check conditions to meet

- input: 
  - nums:list[int] / 1 to 100
    - nums[i]: the amount of money the ith house has / 0 to 100
      - ith house is the neighbor of the i-1th and i+1th house
  - cannot rob two adjacent houses  
- return: the max amount of money one can rob without alerting the police.

## Key idea
        
1. define subproblem in words
- Let R[i] = the max amount of money from house 0th to ith

2. state recursive relation
- base
  - R[0] = nums[0], R[1] = max(nums[0], nums[1])
- Recursive relation: R[i] = max(R[i-1], R[i-2]+nums[i])
        
## Complexity
- time: O(n) because for-loop iteration dominates
- space: O(n) for table R
 
## Caveat and Reflection (Claude-assisted)
- Space can be optimized from O(n) to O(1) by keeping only the last two values (prev1, prev2) instead of the full DP table, since R[i] only depends on R[i-1] and R[i-2]