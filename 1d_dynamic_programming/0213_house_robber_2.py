from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        # R[i][0] = [0,i), R[i][1] = (0,i]
        R = [[0, 0] for _ in range(n)]
        R[1] = [nums[0], nums[1]]
        R[2] = [max(nums[0], nums[1]), max(nums[1], nums[2])]

        for i in range(3, n):
            # to exclude last, nums[i-1] should be added
            R[i][0] = max(R[i - 1][0], R[i - 2][0] + nums[i - 1])
            R[i][1] = max(R[i - 1][1], R[i - 2][1] + nums[i])

        return max(R[-1])


if __name__ == "__main__":
    sol = Solution()
    print(f"The max amount of money is {sol.rob([2, 9, 8, 3, 6])}")  # 15
