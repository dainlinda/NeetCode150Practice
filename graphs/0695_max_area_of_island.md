
# Approach

## Check conditions to meet

- input:
  - grid:list[list[int]]
  - grid[i] = 0(water) or 1(land)
  - 1 <= len(grid), len(grid[i]) <= 50
- return: the max area of an island in grid
  - if no island => 0

## Key idea

- visit all islands using DFS
  - whenever visit a new island, count the area and keep updating global max area 

## Complexity
- when len(grid) = x and len(grid[0])=y
- time: O(xy) for creating visited, O(xy) to find not visited and start explore, aggregated O(xy) to visit islands = O(xy) 
- space: O(xy) for visited, O(xy) for recursion stack (worst case) = O(xy)

## Caveat and Reflection (Claude-assisted)

- Instead of creating visited array, mark visited land as `grid[x][y] = 0` in place
- Recursion depth can reach as deep as 2500 when python's default limit is 1000