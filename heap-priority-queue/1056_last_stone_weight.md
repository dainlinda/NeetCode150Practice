
# Approach

## Check conditions to meet

- input: 
  - stones: list[int]
    - len(stones) = 1 to 20
    - stones[i]: 1 to 100 (x,y: the two heaviest stone)
- repeated action: 
  - if x == y: remove both
  - if x < y: remove x, and y = y-x
- stop: len(stones) <= 1
- return: 
  - stones[0] or 0 when none remain

## Key idea

- use maxheap to get two heaviest stone (pop twice)
- after calculation either no push or push large - second large back
- negate min-heap to get max heap

## Complexity
- time: O(n) for negating the list, O(n) for heapify, O(n) * O(logn) for while loop = O(nlogn)
- space: O(n) for list comprehension
- n decrease on every while iteration
 
## Caveat and Reflection (Claude-assisted)

- Further Optimization:
  - instead of heappop twice and conditional heappush once (current),
  - only heappop y and peek x
    - if y == x, heappop x
    - else heapreplace instead of heappop and heappush(2 sift-down => 1 sift-down)
