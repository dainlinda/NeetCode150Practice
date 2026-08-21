from typing import Optional
from utils.trees import TreeNode, array_to_tree


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n, result = 0, -1

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal n, result
            if not node or n >= k:
                return
            dfs(node.left)
            n += 1
            if n == k:
                result = node.val
                return
            dfs(node.right)

        dfs(root)
        return result


if __name__ == "__main__":
    sol = Solution()
    root = array_to_tree([4, 3, 5, 2, None])
    answer = sol.kthSmallest(root, 4)
    print(f"kth smallest element in this BST is {answer}")  # 5
