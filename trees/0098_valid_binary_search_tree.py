from typing import Optional
from utils.trees import TreeNode, array_to_tree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
            if node is None:
                return True
            if not (node.val > low and node.val < high):
                return False
            # update upper bound for left
            # update lower bound for right
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, -float("inf"), float("inf"))


if __name__ == "__main__":
    solution = Solution()
    root = array_to_tree([5, 4, 8, None, None, 7, 10, 3])

    if solution.isValidBST(root):
        print("It is a valid binary search tree.")
    else:
        print("It is not a valid binary search tree.")
