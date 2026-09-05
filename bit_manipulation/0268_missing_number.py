from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        bitmask = 0
        for num in nums:
            bitmask |= 1 << num
        if "0" not in bin(bitmask)[2:]:
            return max(nums) + 1
        else:
            return bitmask.bit_length() - bin(bitmask)[2:].index("0") - 1


if __name__ == "__main__":
    sol = Solution()
    answer = sol.missingNumber([1, 2, 3])
    print(f"The missing number is {answer}")  # 0
