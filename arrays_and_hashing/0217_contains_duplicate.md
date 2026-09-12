# Approach

## Check conditions to meet

- input: 
  - nums:list[int]
  - 0 <= len(nums) <= 10^5
  - -10^9 <= nums[i] <= 10^9
- return: true if contains duplicate else false

## Key idea

- set remains only unique items so len will be different once we convert array into set

## Complexity
- time: O(n) for set
- space: O(k) for set where k is the cardinality (k<=n)
 
## Caveat and Reflection (Claude-assisted)

- Current one has no early exit, even when a duplicate appears at index 1.
- Time is O(n) *on average*; adversarial hash collisions degrade it to O(n²)