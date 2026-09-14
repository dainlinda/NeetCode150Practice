# Approach

## Check conditions to meet

- input: 
  - s:str / 1 to 1000
    - only digits and english letters
- return:
  - the longest substring of s that is a palindrome.
  - If there are multiple palindromic substrings that have the same length, return any.
## Key idea
        
1. define subproblem in words
- Let lp[j] = the start index and end index of palindrome [start, end] when j is the size of len

1. state recursive relation
- base cases
  - lp[1] = palindrome substrings indicies [start,end] when window size is 1
  - lp[2] = palindrome substrings indicies [start,end] when window size is 2
- lp[j] = {[lp[j-2]'s start -1, lp[j-2]'s end + 1] if s[lp[j-2]'s start-1] == s[lp[j-2]'end+1] for all lp[j-2] elements when lp[j-2]'s start-1 >=0 and lp[j-2]' end+1 <= n-1} when j >= 3


## Complexity
- when n = len(s) 
- time: O(n^2)
  - The number of subproblems: O(n^2)
  - The runtime for table fill: O(n^2)
  - The runtime of return extraction : O(n)
- space: O(n^2) for table lp
 
## Caveat and Reflection (Claude-assisted)
- Further optimizations
  - The same result can be reached with O(n) space by using center-expansion (2n-1 centers, O(1) space per center) instead of storing every [start, end] pair.
  - Manacher's algorithm solves this problem in O(n) time and O(n) space by reusing symmetry information from previously computed palindrome radii, avoiding the O(n²) table entirely.