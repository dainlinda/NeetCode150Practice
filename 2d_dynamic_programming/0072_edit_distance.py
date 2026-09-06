class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        nrow, ncol = len(word1) + 1, len(word2) + 1
        ED = [[0] * (ncol) for _ in range(nrow)]

        # init: base case calc
        for i in range(nrow):
            ED[i][0] = i
        for j in range(ncol):
            ED[0][j] = j

        for i in range(1, nrow):
            for j in range(1, ncol):
                diff = 0 if word1[i - 1] == word2[j - 1] else 1
                ED[i][j] = min(
                    1 + ED[i - 1][j], 1 + ED[i][j - 1], diff + ED[i - 1][j - 1]
                )
        return ED[nrow - 1][ncol - 1]


if __name__ == "__main__":
    sol = Solution()
    word1, word2 = "neatcdee", "neetcode"
    answer = sol.minDistance(word1, word2)
    print(f"The minimum edit distance for '{word1}' and '{word2}' is {answer}")  # 3
