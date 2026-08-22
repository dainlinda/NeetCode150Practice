# Approach

## Check conditions to meet

- a binary tree
  - num nodes: 0 to 10^4
  - node vals: -10^3 to 10^3
- serialization: in-memory ds => a single string
- deserialization: the string => in-memory tree

## Key idea

- use same BFS method used to build array_to_tree in utils.trees

# Correctness check

- off-by-one
  - when deserialize, left and right should be treated at the same time passing array to next index
  - since root is already in deque, `i` should start from 1


## Complexity
- time: 
  - serialize: O(n) for bfs
  - deserialize: O(n) for bfs
- space: 
  - serialize: O(n) for result array
  - deserialize: O(n) for array_tree
 
## Caveat and Reflection (Claude-assisted)
