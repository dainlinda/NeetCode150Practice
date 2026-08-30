
# Approach

## Check conditions to meet

- input: 
  - nums:list[int]
    - a non-empty array
    - Every int appears twice except for one
    - 1 <= len(nums) <= 10^4
    - -10^4 <= nums[i] <= 10^4
- return: the int that appears only once
- O(n) runtime and O(1) extra space

## Key idea

- For O(1) space, use bit mask
  - since it includes negative and zero, add 10000 and minus when return 

## Complexity
- time: O(n) for iterating nums
- space: O(R) where R is the value range (~2*10^4) = effectively O(1) because R is bounded by 10^4
  - O(R) because bitmask grows one bit per value

## Caveat and Reflection (Claude-assisted)

- Python's `^` works on negative ints too (infinite two's complement), so `x ^ x == 0` and `x ^ 0 == x` hold for all values in range.
- The whole problem collapses to `reduce(xor, nums)`, true O(1) space, no offset needed. 