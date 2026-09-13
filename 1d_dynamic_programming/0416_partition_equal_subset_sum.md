# Approach

## Check conditions to meet

- input
  - nums:list[int]
    - 1 <= nums.length <= 100
    - 1 <= nums[i] <= 50
- Return true if you can partition the array into two subsets, where sum(subset1) == sum(subset2). 
  - Otherwise, return false.
  

## Key idea

1. define subproblem in words
- Let cp[i][j] = T if j can be created by a subset of {nums0...numsi-1} where 0<= i <= len(nums) and 0 <= j <= sum(nums)

1. state recursive relation
- return False if sum(nums) is odd
- base 
  - cp[0][j] = F except for j=0 being T
- cp[i][j] = (cp[i-1][j-nums[i-1]] or cp[i-1][j]) if 0 <= j-nums[i]
           = cp[i-1][j] otherwise
- return cp[n][half] when half = sum(nums) / 2

## Complexity
- time: 
  - The number of subproblems: O(sum(nums) * len(nums))
  - The runtime for table fill: O(sum(nums) * len(nums))
  - The runtime of return extraction : O(1)
- space: O(sum(nums) * len(nums)) for table cp
 
## Caveat and Reflection (Claude-assisted)
- Possible optimization
  - Current solution uses a 2D table `cp[i][j]`, but each row only depends on the previous row, so can optimize to a 1D array `cp[j]` of size `total+1`, iterating `j` in descending order per `nums[i]` to avoid overwriting values still needed from the previous row. This reduces space complexity from O(n * total) to O(total), while time complexity stays the same.

- Implication of each element in the algorithm
  - `cp[i-1][j - nums[i-1]]` : can we make j including nums[i-1]
  - `cp[i-1][j]` : can we make j without including nums[i-1] 
  - Taking `or` of these: cp[i][j] only requires some subset of the first i elements to sum to j, not all of them