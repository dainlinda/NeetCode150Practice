from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n, m = len(coins), amount + 1
        cc = [[0] * m for _ in range(n)]
        # base case
        for i in range(n):
            cc[i][0] = 1

        for j in range(1, m):
            for i in range(n):
                cc[i][j] = (cc[i - 1][j] if i > 0 else 0) + (
                    cc[i][j - coins[i]] if j >= coins[i] else 0
                )

        return cc[n - 1][m - 1]


if __name__ == "__main__":
    sol = Solution()
    amount = 4
    coins = [1, 2, 3]
    answer = sol.change(amount, coins)
    print(f"The number of making coin change is {answer}")  # 4
