class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        T = [0] * (n + 1)
        T[1], T[2] = 1, 2

        for i in range(3, n + 1):
            T[i] = T[i - 1] + T[i - 2]
        return T[-1]


if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(f"There are {sol.climbStairs(n)} ways to reach {n}th staircase")
