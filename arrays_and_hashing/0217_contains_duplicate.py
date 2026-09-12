from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 3]
    answer = sol.hasDuplicate(arr)
    print(f"{arr} has {'a duplicate' if answer else 'no duplicate'}")
