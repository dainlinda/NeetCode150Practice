# Approach

## Check conditions to meet

- input: 
  - n:int => 1 to 45
- return:
  - the num of distinct ways to climb to the top of the staircase
    - when n represents the num of steps to reach the top of a staircase
    - and if one can climb with either 1 or 2 steps at a time

## Key idea
        
1. define subproblem in words
- Let CS(i) = the # of ways to arrive stair i

2. state recursive relation
- base
  - CS(1) = 1, CS(2) = 2
- CS(i) = CS(i-1) + CS(i-2) if i>=3
        
## Complexity
- time: O(n) because for-loop iteration dominates
- space: O(n) for table T
 
## Caveat and Reflection (Claude-assisted)

- CS(i) = Fib(i+1)
- Only T[i-1] and T[i-2] are referenced, so two rolling variables suffice => O(n) to O(1) space