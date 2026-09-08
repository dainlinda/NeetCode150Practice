# Approach

## Check conditions to meet

- input: 
  - coins:list[int]
    - 1 <= len(coins) <= 10
    - 1 <= coins[i] <= 2^31 - 1
  - amount:int / 0 to 10^4
  - an unlimited number of each coin
- return:
  - the fewest number of coins that you need to make up the amount
  - If impossible, return -1.

## Key idea
        
1. define subproblem in words
- Let cc[i] = the min number of coins to make up the exact i

2. state recursive relation
- base
  - cc[0] = 0
- Recursive relation: cc[i] = 1 + min(cc[i - coins[j]] if coins[j] <= i)
  - where 0 <= j < len(coins)
        
## Complexity
- when n = amount + 1, m = len(coins)
- time: O(mn)
  - The number of subproblems: O(n)
  - The runtime for table fill: O(mn)
  - The runtime of return extraction : O(1)
- space: O(n) for table cc
 
## Caveat and Reflection (Claude-assisted)
- Possible constant factor optimization
  - Sort coins ascending and break early once coins[j] > i, avoiding unnecessary inner-loop iterations 
  - Filter out coins larger than amount in advance since they can never be used
  - Replace float("inf") with an integer sentinel like amount + 1 to avoid float-int comparison/arithmetic overhead