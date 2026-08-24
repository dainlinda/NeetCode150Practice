from heapq import heappop, heapify
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        npoints = [
            [(point[0] * point[0] + point[1] * point[1]), point] for point in points
        ]
        heapify(npoints)
        return [heappop(npoints)[1] for _ in range(k)]


if __name__ == "__main__":
    sol = Solution()
    answer = sol.kClosest([[0, 2], [2, 0], [2, 2]], 2)
    print(f"K closest points are {answer}")  # [[0,2],[2,0]]
