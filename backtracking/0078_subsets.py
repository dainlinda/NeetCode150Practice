from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        n = len(nums)

        def dfs(combination: List[int]) -> None:
            result.append([nums[i] for i in combination])

            # the most recently added index
            new_i = combination[-1] + 1
            while new_i < n:
                arg = combination + [new_i]
                dfs(arg)
                new_i += 1
            return

        for i in range(n):  # index!! not val
            dfs([i])

        return result


if __name__ == "__main__":
    sol = Solution()
    input_arr = [1, 2, 3]
    out = sol.subsets(input_arr)
    print(f"The subset of {input_arr} is {out}")
