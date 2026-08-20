from collections import deque
from typing import Optional, List
from utils.trees import TreeNode, array_to_tree


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()

                if i == n - 1:
                    result.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return result


if __name__ == "__main__":
    solution = Solution()
    root = array_to_tree([1, 2, 3, 4, None, None, None, 5])
    answer = solution.rightSideView(root)
    print(answer)  # [1, 3, 4, 5]
