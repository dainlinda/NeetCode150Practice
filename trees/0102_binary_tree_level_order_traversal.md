# Approach

## Check conditions to meet

- a binary tree
- input: root of tree
- return: the level order traversal => queue, bfs
  - nested list per level
  - node values!! not node itself
- num nodes: 0 to 2000 => check None!!
- node val: -1000 to 1000

## Key idea
bfs and queue

## Pseudo code 
```
result = []
check edge cases len(tree) = 0 or 1, and return [] or [[root]]

if len(tree) > 1:
    start queue with (root, 0)
    while queue is not empty:
        node, level = dequeue()
        result[level].append(node)
        
        if node.left
            enqueue (node.left, level+1)     
        if node.right
            enqueue (node.right, level+1)
    return result
```

## Complexity
- time: visit all nodes so O(n)
- space: auxiliary space O(max # nodes per level) < O(n), if include result list O(n)

## correctness check
test cases

any edge cases?
- check smallest input
- skewed = [1,None,2,None,3]
 
## Caveat and Reflection
- writing just node to pseudo code made it confusing => node.val is better
- if len(tree) == 1 check is redundant cuz checking existency of left&right

## Feedback from Claude
Q. Can this code be optimized? I believe time: O(n) space: O(max num of nodes per level)

A. Key answer:
- O(n) time (each node dequeued/processed exactly once)
- O(w) space where w is the max width of any level
- For style/efficiency:
  - Storing (node, level) tuples is redundant
    - Since BFS processes nodes strictly in level order, you don't actually need to track the level per node 
    - you can just snapshot len(q) at the top of each iteration of an outer loop, and that count tells you exactly how many nodes belong to the current level. 
    - This avoids the tuple allocation for every node and removes the current_level != level check + reliance on it to know when to open a new sublist. 
    - It's the same asymptotic complexity, but it's the more standard/idiomatic pattern for level-order BFS, and it's a little more robust conceptually
    - your current version works because of an implicit invariant (FIFO order guarantees monotonically non-decreasing levels), while the snapshot approach makes that invariant explicit instead of leaning on it silently.

  - Minor: result[level].append(...) => result[-1].append(...) would be a touch more defensive.