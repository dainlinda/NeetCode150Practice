
# Approach

## Check conditions to meet

- input: 
  - grid:list[list[str]]
    - 1<= col, row <= 100
    - grid[i][j] = '0'(water) or '1'(land)
- return: the num of islands

## Key idea

- create same x*y grid and set all water to visited=True
- use DFS to explore as much as possible changing visited to True
- if it's visited or out of range, then stop exploring

## Complexity
- when len(grid) = x and len(grid[0])=y
- time: O(xy) for visited, O(xy) to make water to be visited, O(xy) to find not visited and start explore, aggregated O(xy) to visit islands = O(xy) 
- space: O(xy) for visited, O(xy) for recursion stack = O(xy)

## Caveat and Reflection (Claude-assisted)

- Since 1 <= #rows, #cols <= 100, the recursion can go as deep as 10^4 when Python's default recursion limit is 10^3
  - use an iterative DFS or a deque-based BFS instead