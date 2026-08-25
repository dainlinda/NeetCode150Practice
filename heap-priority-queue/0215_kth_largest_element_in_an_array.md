
# Approach

## Check conditions to meet

- input: 
  - nums:list[int], unsorted
    - -10^3 <= nums[i] <= 10^3
  - k:int
  - 1 <= k <= len(nums) <= 10^4
- return: the `k`th largest element in `nums`
- Follow-up: with no sorting

## Key idea

- create a k-sized min heap and return root
  - similar to 0703 kth largest element in stream

## Complexity
- time: O(klogk) for heappush, O(nlogk) for heappushpop = O(nlogk)
- space: O(k) for new heap

## Caveat and Reflection (Claude-assisted)

- Full sort: O(n log n)
- k-sized heap: O(n log k)
- Quickselect (average): O(n) average, O(n²) worst-case
- Quickselect + median of medians: O(n) worst-case guaranteed, but with a large constant factor