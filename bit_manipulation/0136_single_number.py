from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bitmask = 0
        for num in nums:
            bitmask ^= 1 << (num + 10000)  # turn it on/off
        return bitmask.bit_length() - 10001


if __name__ == "__main__":
    sol = Solution()
    answer = sol.singleNumber([7, 6, 6, 7, 8])
    print(f"Single number is {answer}")  # 8
