# Approach

## Check conditions to meet

- a binary search tree
- input: the root
- return: kth smallest value (1-indexed)
- 1<=k<=num nodes<=10^4
- node.val = 0 to 10^4

## Key idea

- dfs in-order is the smallest order

## Pseudo code

1. recursively visit the tree via in-order
2. when it's node, increase count
3. if count == k, save node.val as result
4. return result 

# Correctness check
- empty/len=1 input
  - 1<=k<=num nodes so no empty root
  - when len is 1, 
    - dfs(node.left) return instantly (not node)
    - n becomes 1, result becomes node.val
    - dfs(node.right) return instantly (not node)
- duplicates
  - BST doesn't have duplicate
- upper bound
  - python recursion limit is 1000 but skewed tree can go all the way to 10^4
  - either **use iteration** or sys.setrecursionlimit()
- off-by-one
  - n starts from 0 cuz n+=1 before comparison
- early exit
  - need to check n >= k rather than n == k


## Complexity
- time: O(h) for left-most + O(k) for early exit = O(h+k) 
- space: O(h) for recursion stack
  - skewed tree O(n), balanced tree O(logn) 
 
## Caveat and Reflection (Claude-assisted)
- follow-up: frequent modification && kth lookup => order-statistic tree(store left-subtree size per node) => O(h) query, O(h) update