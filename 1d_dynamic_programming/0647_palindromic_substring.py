class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(lptr: int, rptr: int) -> bool:
            while lptr < rptr:
                if s[lptr] != s[rptr]:
                    return False
                lptr += 1
                rptr -= 1
            return True

        n = len(s)
        lp = [[] for _ in range(n + 1)]
        lp[1] = [[i, i] for i in range(n)]
        lp[2] = [[i, i + 1] for i in range(0, n - 1) if is_palindrome(i, i + 1)]

        for j in range(3, n + 1):
            for start, end in lp[j - 2]:
                start -= 1
                end += 1
                if start >= 0 and end <= n - 1 and s[start] == s[end]:
                    lp[j].append([start, end])
        total = 0
        for ith_list in lp:
            total += len(ith_list)
        return total


if __name__ == "__main__":
    sol = Solution()
    s = "aaa"
    print(
        f"The number of palindromic substring of '{s}' is {sol.countSubstrings(s)}"
    )  # 6
