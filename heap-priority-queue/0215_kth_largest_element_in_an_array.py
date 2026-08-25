from typing import List
from heapq import heappush, heappushpop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        i = 0
        while i < len(nums):
            if len(heap) < k:
                heappush(heap, nums[i])
            else:  # once heap size reaches k
                heappushpop(heap, nums[i])
            i += 1

        return heap[0]


if __name__ == "__main__":
    sol = Solution()
    answer = sol.findKthLargest([2, 3, 1, 5, 4], 2)
    print(f"Kth largest element in an array is {answer}")  # 4
