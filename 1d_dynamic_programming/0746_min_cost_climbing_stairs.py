from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        F = [0] * (n + 1)  # F[0], F[1] = 0, 0

        for i in range(2, n + 1):
            F[i] = min(F[i - 1] + cost[i - 1], F[i - 2] + cost[i - 2])
        return F[-1]


if __name__ == "__main__":
    sol = Solution()
    answer = sol.minCostClimbingStairs([1, 2, 1, 2, 1, 1, 1])
    print(f"The min cost to climb the stairs is {answer}")  # 4
