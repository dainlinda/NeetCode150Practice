from utils.trees import TreeNode, array_to_tree
from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = -float("inf")

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal global_max

            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            local_max = max(node.val, node.val + left, node.val + right)
            sat_path = node.val + left + right
            global_max = max(global_max, sat_path, local_max)

            return local_max

        dfs(root)
        return global_max


if __name__ == "__main__":
    sol = Solution()
    root = array_to_tree([-15, 10, 20, None, None, 15, 5, -5])
    print(f"The max path sum is {sol.maxPathSum(root)}")  # 40
