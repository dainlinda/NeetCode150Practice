from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount + 1
        cc = [float("inf")] * n
        cc[0] = 0
        for i in range(1, n):
            local_min = float("inf")
            for j in range(len(coins)):
                if coins[j] <= i and local_min > cc[i - coins[j]] + 1:
                    local_min = cc[i - coins[j]] + 1
            cc[i] = local_min
        return cc[amount] if cc[amount] != float("inf") else -1


if __name__ == "__main__":
    sol = Solution()
    coins = [1, 5, 10]
    amount = 12
    answer = sol.coinChange(coins, amount)
    print(f"The min num of coin is {answer}")  # 3
