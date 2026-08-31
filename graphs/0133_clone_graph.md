
# Approach

## Check conditions to meet

- input: a root of a graph
  - a connected, undirected graph
- return: a deep copy of the graph

- 0 <= the num of nodes in the graph <= 100
- 1 <= node.val <= 100
- no duplicate edges & no self-loops

## Key idea

- Iterate the graph using DFS, maintaining new nodes in a dictionary(id of origin node: copied Node() object)
  - keep adding not visited neighbors to stack
  - append a new neighbor to new node's neighbors list
    - if the neighbor is not visited, create a new node first
- return copied first node using id(first node) as a key to dict 

## Complexity
- When the num of vertices(nodes) is V and the num of edges is E
- time: O(V + E) for visiting all nodes and their neighbors
  - worst case = clique (E = V(V-1)/2) = O(V^2)
- space: O(V) for stack + O(V) for copies = O(V)

