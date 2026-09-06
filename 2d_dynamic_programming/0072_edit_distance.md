# Approach

## Check conditions to meet

- input: 
  - word1:str, word2:str
    - each consisting of lowercase English letters
- return:
  - the minimum # of edits(insert, delete, replace) to make word1 equal word2.

## Key idea
        
1. define subproblem in words
- Let ED(i,j) = the min # of edits to make word1[0...i] equal word2[0...j]

1. state recursive relation
- base 
  - ED(i,0) = i, ED(0,j) = j because only either of one letter exists.
- ED(i,j) = min(1+ED(i-1,j), 1+ED(i,j-1), diff + ED(i-1, j-1) when i, j>0)
  - diff= 0 if word1[i-1] == word2[j-1] otherwise 1 
    - i-1 and j-1 because we are including 0 (no char for one word)
- return ED(m, n) when m = len(word1) and n = len(word2)

## Complexity
- time: O(mn)
  - The number of subproblems: O(mn)
  - The runtime for table fill(ED):O(mn)
  - The runtime of return extraction : O(1)
- space: O(mn) for table ED
 
## Caveat and Reflection (Claude-assisted)
- Space complexity can be optimized from O(mn) to O(min(m,n)) using a rolling array, since computing row i only requires row i-1. This works because we only need the final edit distance, **not the backtracking path**