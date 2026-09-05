
# Approach

## Check conditions to meet

- input: 
  - nums:list[int]
    - 1<=len(nums)<=1000
    - containing n integers in the range [0, n] 
    - without any duplicates
- return: the single number in the range that is missing from nums.
    - O(1) space O(n) time required.

## Key idea

- For O(1) space, use bit mask
  - fill the bitmask by adding 1 << each num
  - find index of 0, and negate it from bitmask length 
    - additional -1 because it starts from 0
  - if there's no 0, then return max(nums)+1

## Complexity
- time: O(n) for iterating nums, O(n) for slicing bitmask, O(n) for finding max(nums) = O(n)
- space: O(n) for bitmask

## Caveat and Reflection (Claude-assisted)

- The bitmask grows with n, so space complexity is actually O(n), not O(1) — the standard O(1) space solution uses XOR accumulation instead.