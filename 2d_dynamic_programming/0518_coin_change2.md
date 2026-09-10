# Approach

## Check conditions to meet

- input: 
  - coins:list[int]
    - 1 <= len(coins) <= 100
    - 1 <= coins[i] <= 5000
  - amount:int / 0 to 5000
  - an unlimited number of each coin
  - each value in coins is unique.
- return:
  - the number of distinct combinations that total up to amount
  - If impossible, return 0

## Key idea

1. define subproblem in words
- Let cc[i][j] = the number of distinct combinations that total up to j when coins[0]..coins[i] are used

2. state recursive relation
- base
  - cc[i][0] = 1 
- Recursive relation: 
  - cc[i][j] = {cc[i-1][j] if i>0 else 0}
             + {cc[i][j-coins[i]] if coins[i] <=j else 0}
  - when 0 <= i < len(coins) and 1 <= j <=amount
  - return cc[len(coins)-1][amount]
        
## Complexity
- when n = len(coins), m = amount + 1 
- time: O(mn)
  - The number of subproblems: O(mn)
  - The runtime for table fill: O(mn)
  - The runtime of return extraction : O(1)
- space: O(mn) for table cc
 
## Caveat and Reflection (Claude-assisted)
- Python's negative indexing wraps silently instead of raising, so the unguarded recurrence read garbage cells at `i=0` and `j<coins[i]`
- Only the previous row and the current row are read, so the O(mn) table can be collapsed to a single O(m) array.