from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]  # negate them
        heapify(stones)
        while len(stones) > 1:
            y, x = heappop(stones), heappop(stones)
            if -y > -x:
                heappush(stones, y - x)
        return -stones[0] if stones else 0


if __name__ == "__main__":
    sol = Solution()
    last = sol.lastStoneWeight([2, 3, 6, 2, 4])
    print(f"The weight of last stone is {last}")  # 1
