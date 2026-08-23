
# Approach

## Check conditions to meet

- input: 
  - k : 1 to 10^3 
  - nums: 
    - len: 0 to 10^3
    - nums[i]: -10^3 to 10^3
    - include duplicates
    - not sorted
  - val: -10^3 to 10^3
- return: the kth largest int (include val to calc)
  - answer always exist

## Key idea

- use max heap and pop k times and return last popped item
  - multiply -1 to change min heap to max heap
  - after kth heappop, restore the heap

## Complexity
- time: 
  - __init__: O(n) for list comprehension, O(n) for heapify = O(n)
  - add: O(2*k*logn) for pop and restore = O(klogn)
- space: 
  - __init__: O(n) for self.nums
  - add: O(k) for popped
- n increases on every add

## Caveat and Reflection (Claude-assisted)

- Model solution: a min heap of size k 
  - __init__: if len(nums) > k, reduce size to be k
  - add: 
    - push when heap size < k
    - heappushpop once size reaches k to maintain k size
    - return heap[0]
    - time: O(log k) fixed time for push and heappushpop 
    - space: O(k) fixed space
