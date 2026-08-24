
# Approach

## Check conditions to meet

- input: 
  - 2-D array points where points[i] = [xi, yi]
    - 1<=k<=len(points)<=1000
    - xi, yi: -100 to 100
- return: the k closest points to the origin (0,0)
  - the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2))
  - any order
  - Guaranteed to be unique.


## Key idea

- create a min heap with weight being its distance to origin

## Complexity
- time: O(n) for list comprehension, O(n) for heapify, O(klogn) for heappop = O(n) + O(klogn) = O(nlogn) if k == n
- space: O(n) for list comprehension (Auxiliary space) 

## Caveat and Reflection (Claude-assisted)

- sqrt is unnecessary to decide k closest
  - pow => x*x to reduce function call overhead

- Possible optimizations 
  - Size-k max-heap: 
    - maintain a heap of only k elements (negate distances to simulate max-heap in Python) 
    - time: O(n log k) time
    - space: O(k) 
    - better when k <<< n, negligible when k ≈ n
  - Quickselect : partition-based selection 
    - Refer: CS 6515 GA note taking - DC2 Fast Select
    - time: average O(n) / worst O(n²)
    - space: O(1) for iteration / average O(logn) worst O(n) for recursion
    - optimal since output order doesn't matter
    - but more complex to implement correctly