from typing import Optional
from utils.trees import TreeNode, array_to_tree


# time: O(n*m), space: O(h)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not (p or q):
                return True

            stack = [(p, q)]
            while stack:
                node1, node2 = stack.pop()
                if not (node1 or node2):  # if not both
                    continue
                if not node1 or not node2 or node1.val != node2.val:
                    return False
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
            return True

        # explore possible starting points
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue

            if node.val == subRoot.val and is_same_tree(node, subRoot):
                return True

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False


if __name__ == "__main__":
    root = array_to_tree([1, 2, 3, 4, 5])
    subRoot = array_to_tree([2, 4, 5])
    solution = Solution()
    result = solution.isSubtree(root, subRoot)
    if result:
        print("It is a subtree.")
    else:
        print("It is not a subtree.")
