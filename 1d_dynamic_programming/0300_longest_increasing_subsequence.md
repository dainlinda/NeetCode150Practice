# Approach

## Check conditions to meet

- input: 
  - nums:list[int] / 1 to 1000
    - nums[i]: -1000 to 1000
- return:
  - the length of the longest **strictly increasing** subsequence.
## Key idea
        
1. define subproblem in words
- Let LIS(i) = the length of the strictly increasing longest subsequence ending at index i

1. state recursive relation
- base 
  - LIS(0) = 1
- LIS(i) = 1 + max(LIS(j) : 0<= j <= i-1 : when nums[i] > nums[j])

## Complexity
- time: O(n^2)
  - The number of subproblems: O(n)
  - The runtime for table fill(LIS): 1+2+...+n = O(n(n-1)/2) = O(n^2)
  - The runtime of return extraction : O(n) for max
- space: O(n) for table LIS
 
## Caveat and Reflection (Claude-assisted)

- This O(n^2) approach can be optimized to O(n log n) using patience sorting with binary search
  - Maintain an array `tails`, where tails[k] is the smallest possible tail value of an increasing subsequence of length k+1. 
  - Since tails stays sorted at all times, each new element can be placed via binary search (either extending tails or replacing the first element >= it), rather than scanning all previous elements.