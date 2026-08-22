# Approach

## Check conditions to meet

- input: preorder list & inorder list (same length, 1 to 2001)
  - nodes val: -10^4 to 10^4
- return: the root of binary tree

## Key idea

- use preorder to check where the root is
- use inorder to divide left subtree and right subtree

## Neetcode Hint Reference
- (Hint 5) We use Depth First Search (DFS) to construct the tree. A global variable tracks the current index in the pre-order array. Indices l and r represent the segment in the in-order array for the current subtree. For each node in the pre-order array, we create a node, find its index in the in-order array using the hash map, and recursively build the left and right subtrees by splitting the range [l, r] into two parts for the left and right subtrees.

## Pseudo code

```
repeat
    check root from preorder
    by using that root, divide inorder 
        from left to root-1 for left subtree
        from root+1 to right for right subtree
```

## Complexity
- time: O(n) for visiting all nodes recursively
- space: O(h) for recursion stack + O(n) for indict = O(n)
 
## Caveat and Reflection (Claude-assisted)

- An earlier version of dfs error caught by Claude:
  - Early return skipped the right subtree. 
    - The old version returned as soon as the left recursive call signaled "no children," 
    - so the code that builds node.right was never reached whenever a left child was a leaf.
  - No emptiness check before creating a child. 
