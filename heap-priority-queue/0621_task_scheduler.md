
# Approach

## Check conditions to meet

- input:
  - tasks:list[char], 1 to 10^4
    - char = A to Z
  - n:int, 0 to 100
- a task per cpu cycle, in any order
  - identical1 - n cycles - identical2
- return: min # of cpu cycles to complete all tasks

## Key idea (Referenced Hint 4)

- We start by calculating the frequency of each task and initialize a variable time to track the total processing time. The task frequencies are inserted into a Max-Heap. We also use a queue to store tasks along with the time they become available after the cooldown. At each step, if the Max-Heap is empty, we update time to match the next available task in the queue, covering idle time. Otherwise, we process the most frequent task from the heap, decrement its frequency, and if it's still valid, add it back to the queue with its next available time. If the task at the front of the queue becomes available, we pop it and reinsert it into the heap.


## Complexity
- When m = len(tasks) and k = the number of unique tasks
  - since k is bounded by 26, O(k) = O(1)

- time: O(m)
  - init: O(m) for Counter + O(k) for creating a max_heap + O(k) for heapify = O(m)
  - while loop: O(m)
    - loop iteration: O(m)
    - if max_heap: O(logk) for heappop = O(1)
    - if task_q[0][0] == curr_time: O(logk) for heappush = O(1)

- space: O(k) for count + O(k) for max_heap and task_q = O(k) = O(1)

## Caveat and Reflection (Claude-assisted)

- The answer can be as large as (max_freq - 1) * (n + 1) + count, yet the loop runs O(m) iterations. Runtime is therefore bounded by the number of tasks, not by the returned time.
