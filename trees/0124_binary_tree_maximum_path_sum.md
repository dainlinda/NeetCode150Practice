# Approach

## Check conditions to meet

- a non-empty binary tree
- input: the root of the tree
  - num nodes: 1 to 3 * 10^4
  - node val: - 10^3 to 10^3 
- return: the max path sum of any non-empty path
- sequence of nodes => linear!! 
  - no branch

## Key idea

- path can go maximum two different directions among (L, R, parent)
- start from leaf nodes for accumulation
  - Maintain global max (init with -inf)
  - accumulate sum: local max(node, node+L, node+R) 
    - compare global max against node+L+R, and update global max
      - this one is already saturated with two directions so don't pass to parent 
      - pass local max to parent and repeat comparison 
- DFS cuz it's path, and post-order to visit root the last

## Pseudo code

```
var global_max = -inf

def dfs(node):
    if not node:
        return 0
    left = dfs(node.left) 
    right = dfs(node.right)
    
    local_max = max(node.val, node.val + left, node.val + right)
    saturated_path = node.val + left + right

    global_max = max(global_max, saturate_path, local_max)
    return local_max # children -> parent

dfs(root)
return global_max
```

# Correctness check

- when there are only negative values
  - say [-10, -1]
  - when it's leaf node(-1), it will update global_max to -1
    - node.val = -1, node.val + left = -1, node.val + right = -1, node.val + left + right = -1
  - when it sends -1 to root node(-10), it won't be able to update global_max
  - -1 is returned successfully
- empty/len=1 input
  - a non-empty binary tree
  - if len=1, then it will only execute one time comparing node.val with global max
- duplicates
  - does not matter here
- upper bound
  - recursion can fail if it's skewed tree since python's max recursion depth is 1000, but the num nodes can be 3 * 10^4
    - => iterative post-order is better
- off-by-one
  - no off-by-one to consider
- early exit
  - we should explore all nodes so early exit is not possible

## Complexity
- time: O(n) for visiting all nodes via postorder dfs
- space: O(h) for recursion stack
  - O(n) for skewed tree, O(logn) for balanced tree
 
## Caveat and Reflection (Claude-assisted)

- Possible Optimization
  - Clamping each child's return at 0 (`left = max(dfs(node.left), 0)`) collapses the four-candidate enumeration into `global_max = max(global_max, node.val + left + right)` and `return node.val + max(left, right)`. 
  - The two are equivalent because `max(v, v+L, v+R, v+L+R) = v + max(0, L, R, L+R)` equals `v + max(L, 0) + max(R, 0)` in all three sign cases — the standalone `node.val` candidate is what plays the role of the clamp. 
  - With `L, R >= 0`, `v+L+R >= v+max(L,R)`, so the single-branch case is subsumed and only one `global_max` comparison is needed. 
  - Same O(n) time and O(h) space either way; 
  - the clamped form is just fewer operations and reads more directly as "best downward path through this node."