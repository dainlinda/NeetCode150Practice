from utils.trees import TreeNode, array_to_tree


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        ancestor = node = root
        while True:
            if p.val < node.val and q.val < node.val:
                node = node.left
                ancestor = node
            elif p.val > node.val and q.val > node.val:
                node = node.right
                ancestor = node
            else:  # diverge or either = node
                return ancestor


if __name__ == "__main__":
    solution = Solution()
    root = array_to_tree([5, 3, 8, 1, 4, 7, 9, None, 2])
    p, q = TreeNode(1), TreeNode(2)
    answer = solution.lowestCommonAncestor(root, p, q)
    print(f"The least common ancestor is {answer.val}")
