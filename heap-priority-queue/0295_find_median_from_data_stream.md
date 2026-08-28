
# Approach

## Check conditions to meet

- Implement the MedianFinder class
  - MedianFinder()
    - initializes the `MedianFinder` object
  - void addNum(int num)
    - adds the integer `num` from the data stream to the data structure
    - -10^5 <= num <= 10^5
    - At most 5*10^4 calls
  - double findMedian()
    - return: the median of all elements so far
    - At most 5*10^4 calls
    - only be called after adding at least one integer to the data structure.

## Key idea

- maintain a max-heap for small half and a min-heap for large half
  - if even len => return average of two roots
  - if odd len => return smaller root
- invariant : len(small half) = len(large half) + 0 or 1

## Complexity
- time: 
  - addNum: O(logn) for heappush, heappop
  - findMedian: O(1)
- space: O(n) for both max_heap and min_heap

## Caveat and Reflection (Claude-assisted)

- Follow-ups: 
  - when we know data distribution:
  - if all values are in [0, 100]: 
    - use a 101-sized array. O(1) addNum and O(1) findMedian because scan is maximum 101
  - if only 99% are in [0, 100]: 
    - use a 101-sized array and handle the two tails separately
      - if x < 0 then lower tail, if x > 100 then upper tail => heap or ordered list.
    - when searching for median, 
      - if idx < len(lower_tail) => lower tail
      - elif idx < len(lower_tail) + bucket_total => 101-sized array
      - else => upper tail