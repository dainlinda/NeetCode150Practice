class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(lptr: int, rptr: int) -> bool:
            while lptr < rptr:
                if s[lptr] != s[rptr]:
                    return False
                lptr += 1
                rptr -= 1
            return True

        n = len(s)
        if n == 1:
            return s[0]

        lp = [[] for _ in range(n + 1)]
        lp[1] = [[i, i] for i in range(n)]
        lp[2] = [[i, i + 1] for i in range(0, n - 1) if is_palindrome(i, i + 1)]

        for j in range(3, n + 1):
            for start, end in lp[j - 2]:
                start -= 1
                end += 1
                if start >= 0 and end <= n - 1 and s[start] == s[end]:
                    lp[j].append([start, end])
        while True:
            candidates = lp.pop()
            if candidates:
                start, end = candidates[0]
                return s[start : end + 1]


if __name__ == "__main__":
    sol = Solution()
    s = "ababc"
    answer = sol.longestPalindrome(s)
    print(f"The longest palindromic substring for '{s}' is '{answer}'")  # aba or bab
