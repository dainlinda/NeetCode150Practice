# Approach

## Check conditions to meet

- a binary tree
- return: the values of the nodes / visible from right side
  - order: top-down
- input: root node
- num nodes: 0 to 100 => None check
  - val: -100 to 100

## Key idea
Right side nodes => root + right most node per level

## Pseudo code 
```
return [] if not root

if root:
  do BFS
  check len(q) for every iteration
  append i == len(q)-1 to result
```

## Complexity
- time: visit all nodes so O(n)
- space: auxiliary space O(max # nodes per level)

## correctness check
test cases
edge cases
 
## Caveat and Reflection
- try with dfs next time

## Feedback from Claude