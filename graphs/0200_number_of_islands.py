from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_row, num_col = len(grid), len(grid[0])
        visited = [[False] * num_col for _ in range(num_row)]

        for x in range(num_row):
            for y in range(num_col):
                if grid[x][y] == "0":
                    visited[x][y] = True

        num_islands = 0

        def explore(x: int, y: int):
            if x < 0 or x >= num_row or y < 0 or y >= num_col or visited[x][y]:
                return  # stop explore
            visited[x][y] = True

            explore(x, y - 1)  # left
            explore(x, y + 1)  # right
            explore(x + 1, y)  # down
            explore(x - 1, y)  # up

        for x in range(num_row):
            for y in range(num_col):
                if not visited[x][y]:
                    num_islands += 1
                    explore(x, y)

        return num_islands


if __name__ == "__main__":
    sol = Solution()
    answer = sol.numIslands(
        [
            ["1", "1", "0", "0", "1"],
            ["1", "1", "0", "0", "1"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
    print(f"The number of islands is {answer}")  # 4
