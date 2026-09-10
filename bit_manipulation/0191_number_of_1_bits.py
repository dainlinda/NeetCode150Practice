class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


if __name__ == "__main__":
    sol = Solution()
    answer = sol.hammingWeight(2147483645)
    print(f"The number of 1 bits is {answer}")  # 30
