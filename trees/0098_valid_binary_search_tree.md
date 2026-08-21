# Approach

## Check conditions to meet

- input: a binary tree root
  - num nodes: 1 to 10^4
  - nodes val: -10^8 to 10^8
- return: true if valid else false
  - valid: node.left.val < node.val < node.right.val (recursively)
    - equal to => invalid

## Key idea

- like 1448 good nodes, should record previous ancestors on the way
  - dfs: either recursion or iteration passing info
- (Hint) Tracking an interval that defines the lower and upper limits for the node's value in that subtree. This interval will be updated as we move down the tree, ensuring each node adheres to the BST property.

## Pseudo code
recursively passing interval (a, b) as an argument where a < node.val < b
update upper bound when traverse left, lower when traverse right
start to return False if it's not met

## Complexity
- time: visit all nodes so O(n)
- space: O(h) for recursion stack
  - O(n) when skewed, O(logn) when blanced
 
## Caveat and Reflection (Claude-assisted)
- Do not use the value that can be returned by correct program as a sign of incorrectness
  - e.g. used -1 for failure and node.val for success for the first attempt, which failed cuz node.val can be -1 
- Instead of hardcoding, using float("-inf") and float("inf") keeps things safe
- For a boolean check function, no reason to return node.val 
- Early termination via and short-circuiting    
- The other approach: in-order traversal (iterative version)
  - keep track of the single previously visited value and check that it's less than the current one
