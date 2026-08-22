from utils.trees import TreeNode, preorder_print_tree
from typing import Optional, List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indict = {v: i for i, v in enumerate(inorder)}
        node = TreeNode(preorder[0])

        # preorder: start to end(exclusive), inorder: instart
        def dfs(node: TreeNode, start: int, end: int, instart: int) -> None:
            i = indict[node.val]
            left_size = i - instart
            ridx = start + left_size

            if left_size > 0:
                node.left = TreeNode(preorder[start])
                dfs(node.left, start + 1, ridx, instart)  # left

            if end - ridx > 0:
                node.right = TreeNode(preorder[ridx])
                dfs(node.right, ridx + 1, end, i + 1)  # right

        dfs(node, 1, len(preorder), 0)

        return node


if __name__ == "__main__":
    sol = Solution()

    result = sol.buildTree(preorder=[1, 2, 3, 4], inorder=[2, 1, 3, 4])
    preorder_print_tree(result)
