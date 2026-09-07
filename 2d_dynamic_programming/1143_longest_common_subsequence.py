class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        nrow, ncol = len(text1) + 1, len(text2) + 1
        LCS = [[0] * ncol for _ in range(nrow)]

        for i in range(1, nrow):
            for j in range(1, ncol):
                diff = 1 if text1[i - 1] == text2[j - 1] else 0
                LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1], diff + LCS[i - 1][j - 1])
        return LCS[nrow - 1][ncol - 1]


if __name__ == "__main__":
    sol = Solution()
    text1, text2 = "cat", "crabt"
    answer = sol.longestCommonSubsequence(text1, text2)
    print(f"The longest common subsequence for {text1} and {text2} is {answer}")  # 3
