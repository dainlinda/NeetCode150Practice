# Approach

## Check conditions to meet

- input: 
  - text1:str, text2:str
    - 1 <= len(text1), len(text2) <= 1000
    - text1 and text2 consist of only lowercase English characters
- return:
  - the length of the longest common subsequence between the two strings if one exists 
  - otherwise return 0.

## Key idea
        
1. define subproblem in words
- Let LCS(i,j) = the longest common subsequence for text1[0...i] and text2[0...j]

2. state recursive relation
- base 
  - LCS(i,0) = 0, LCS(0,j) = 0 because an empty string has no match with other characters.
- LCS(i,j) = max(LCS(i-1,j), LCS(i,j-1), diff+LCS(i-1,j-1) when i,j > 0)
  - diff = 1 if text1[i-1] == text2[j-1] otherwise 0
- return LCS(m, n) when m = len(text1) and n = len(text2)

- example 2D table
```
  - c r a b t
- 0 0 0 0 0 0
c 0 1 1 1 1 1 
a 0 1 1 2 2 2
t 0 1 1 2 2 3
```

## Complexity
- time: O(mn)
  - The number of subproblems: O(mn)
  - The runtime for table fill(LCS):O(mn)
  - The runtime of return extraction : O(1)
- space: O(mn) for table LCS
 
## Caveat and Reflection (Claude-assisted)
- Space complexity can be optimized from O(mn) to O(min(m,n)) using a rolling array, since computing row i only requires row i-1.
