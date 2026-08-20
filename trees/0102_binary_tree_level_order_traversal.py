from collections import deque
from typing import Optional, List
from utils.trees import TreeNode, array_to_tree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # edge cases
        if not root:
            return []

        # len(tree) > 0
        result = []
        q = deque([root])
        while q:
            result.append([])

            for _ in range(len(q)):
                node = q.popleft()
                result[-1].append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result


if __name__ == "__main__":
    solution = Solution()
    root = array_to_tree([1, None, 2, None, 3])
    answer = solution.levelOrder(root)
    print(answer)  # [[1], [2], [3]]
