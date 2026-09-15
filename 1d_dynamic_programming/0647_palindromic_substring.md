# Approach

## Check conditions to meet

- input: 
  - s:str / 1 to 1000
    - consists of lowercase English letters.
- return:
  - the number of substrings within s that are palindromes

## Key idea

- Refered: 0005 longest palindromic substring
1. define subproblem in words
- Let lp[j] = [the start index and end index of palindrome [start, end] pairs when j is the size of len]

1. state recursive relation
- base cases
  - lp[1] = palindrome substrings indicies [start,end] when window size is 1
  - lp[2] = palindrome substrings indicies [start,end] when window size is 2
- lp[j] = {[lp[j-2]'s start -1, lp[j-2]'s end + 1] if s[lp[j-2]'s start-1] == s[lp[j-2]'end+1] for all lp[j-2] elements when lp[j-2]'s start-1 >=0 and lp[j-2]' end+1 <= n-1} when j >= 3
- return total count of elements of lp


## Complexity
- when n = len(s) 
- time: O(n^2)
  - The number of subproblems: O(n^2)
  - The runtime for table fill: O(n^2)
  - The runtime of return extraction : O(n^2)
- space: O(n^2) for table lp
 
## Caveat and Reflection (Claude-assisted)
- Expand around center: 
  - O(n^2) time, O(1) space 
  - expand from each of the 2n-1 centers, counting on each valid expansion instead of storing intervals
- Manacher's algorithm: 
  - O(n) time, O(n) space
  - computes palindrome radius at every center in linear time via mirror reuse, then sums (radius+1)//2.