from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2

        cp = [[False] * (total + 1) for _ in range(n + 1)]

        # base case
        for j in range(total + 1):
            cp[0][j] = False
        cp[0][0] = True

        for i in range(1, n + 1):
            for j in range(total + 1):
                if 0 <= j - nums[i - 1]:
                    cp[i][j] = cp[i - 1][j - nums[i - 1]] or cp[i - 1][j]
                else:
                    cp[i][j] = cp[i - 1][j]
        return cp[n][half]


if __name__ == "__main__":
    sol = Solution()
    answer = sol.canPartition([1, 2, 3, 4])
    print(f"We {'can' if answer else 'cannot'} partition this array")
