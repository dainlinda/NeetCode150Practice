# Approach

## Check conditions to meet

- input: 
  - cost:list[int]
    - 2 <= len(cost) <= 100
    - 0 <= cost[i] <= 100
- return:
  - the min cost to reach the top of the staircase (i.e. len(cost)th stair)
    - when cost[i] is the cost of taking a step from the ith floor,
    - one can choose to start at either the index 0 or the index 1 floor,
    - and one can step to either the (i+1)th floor or the (i+2)th floor after paying. 

## Key idea
        
1. define subproblem in words
- Let F[i] = the min cost to arrive at the ith floor
        
2. state recursive relation
- base
  - F[0] = 0, F[1] = 0
- F[i] = min(F[i-1] + cost[i-1], F[i-2]+cost[i-2]) when i>=2
        
## Complexity
- time: O(n) because for-loop iteration dominates
- space: O(n) for table F
 
## Caveat and Reflection (Claude-assisted)

- Used n+1 sized table because top is F[n]
- Space can be reduced to O(1) since F[i] only depends on F[i-1] and F[i-2] by keeping two rolling variables