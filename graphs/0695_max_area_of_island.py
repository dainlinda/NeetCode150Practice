from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        visited = [[False] * ncol for _ in range(nrow)]

        def explore(x: int, y: int) -> int:
            if (
                x < 0
                or y < 0
                or x >= nrow
                or y >= ncol
                or visited[x][y]
                or grid[x][y] == 0
            ):
                return 0

            visited[x][y] = True

            u = explore(x - 1, y)  # up
            d = explore(x + 1, y)  # down
            l = explore(x, y - 1)  # left
            r = explore(x, y + 1)  # right

            return u + d + l + r + 1

        # starting point
        max_area = 0
        for i in range(nrow):
            for j in range(ncol):
                if not visited[i][j] and grid[i][j] == 1:
                    area = explore(i, j)
                    max_area = max(max_area, area)
        return max_area


if __name__ == "__main__":
    sol = Solution()
    answer = sol.maxAreaOfIsland(
        [[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]
    )
    print(f"The max area of an island is {answer}")  # 6
