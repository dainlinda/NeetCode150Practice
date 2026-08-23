from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k

        # heapify negated
        self.nums = [-num for num in nums]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        # add negated val
        heapq.heappush(self.nums, -val)

        # pop k times
        popped = [heapq.heappop(self.nums) for _ in range(self.k)]

        # last popped item is kth largest
        result = popped[-1]

        # restore popped vals
        for p in popped:
            heapq.heappush(self.nums, p)  # already negated vals

        return -result  # negate back


if __name__ == "__main__":
    kth_largest = KthLargest(3, [1, 2, 3, 3])
    print(kth_largest.add(3))  # return 3
    print(kth_largest.add(5))  # return 3
    print(kth_largest.add(6))  # return 3
    print(kth_largest.add(7))  # return 5
    print(kth_largest.add(8))  # return 6
