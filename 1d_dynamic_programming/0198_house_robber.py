from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        R = [0] * n
        R[0] = nums[0]
        R[1] = max(nums[0], nums[1])

        for i in range(2, n):
            R[i] = max(R[i - 1], R[i - 2] + nums[i])
        return R[-1]


if __name__ == "__main__":
    sol = Solution()
    print(f"The maximum amount of money is {sol.rob([2, 9, 8, 3, 6])}")  # 16
