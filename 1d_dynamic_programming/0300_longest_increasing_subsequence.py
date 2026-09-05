from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1] * n

        for i in range(n):
            local_max = 0
            for j in range(i):  # j <= i-1
                if nums[i] > nums[j] and local_max < LIS[j]:
                    local_max = LIS[j]
            LIS[i] = 1 + local_max

        return max(LIS)


if __name__ == "__main__":
    sol = Solution()
    answer = sol.lengthOfLIS([9, 1, 4, 2, 3, 3, 7])
    print(f"The length of longest increasing subsequence is {answer}")  # 4
