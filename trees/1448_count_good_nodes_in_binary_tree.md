# Approach

## Check conditions to meet

- a binary tree 
- good nodes
  - root to node x, x.val >= all others val
    - no greater than => smaller than or equal to
- input: root node
- return: the num of good nodes (count meeting the condition)
- num nodes: 1 to 10^5
- val: -100 to 100

## Key idea
monotonically increasing => monotonic stack
dfs to maintain ancestors per path

## Pseudo code

```
var result = 1

array stack = [root]
array mono = [root]
set visited = {root}

while stack is not empty:
    node = peek stack[-1]

    stack.append(node.left) if exist and not visited
    stack.append(node.right) if exist and not visited

    if node.val >= mono[-1] and mono[-1] is not itself:
        mono.append(node)

    if it's leaf node or visited all children:
        node = stack.pop() # visit for real
        if mono[-1] is itself:
            mono.pop()
        if mono is empty:
            break
        if mono[-1].val <= node.val:
            result++
        visited.add(node)
return result
```

## Complexity
- time: visit all nodes twice 2 * O(n) = O(n)
- space: O(# good nodes) for mono => O(h) + O(# nodes located in longest path) for stack => O(h) + O(n) for visited = O(n)

## correctness check
test cases
edge cases
 
## Caveat and Reflection
- working solution but not optimized solution
- obsessed with monotonic stack too much

## Adapted Feedback from Claude
- Where it actually breaks: == vs is
  - mono[-1] == node, mono[-1] != node, and the visited dictionary keys all depend on how TreeNode defines __eq__ / __hash__
    - use (is / is not) && id(node) as a key
- Design note
  - Instead of maintaining mono as a stack, if the stack held (node, max_so_far) pairs, both mono and visited disappear entirely and space drops to O(h). 
  - This looks like a case where committing to the "monotonic stack" frame up front made the structure heavier than it needed to be 
  - The problem is really "propagate the path maximum downward," which is more naturally handled by attaching state to the node.