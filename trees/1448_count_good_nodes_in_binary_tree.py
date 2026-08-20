from collections import defaultdict
from utils.trees import TreeNode, array_to_tree


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 1  # root
        stack, mono, visited = [root], [root], defaultdict(bool)

        def is_leaf(node: TreeNode) -> bool:
            return not (node.left or node.right)

        def is_children_visited(node: TreeNode) -> bool:
            nonlocal visited
            lbool, rbool = True, True  # default to True if None
            if node.left is not None:
                lbool = visited[id(node.left)]
            if node.right is not None:
                rbool = visited[id(node.right)]
            return lbool and rbool

        while stack:
            node = stack[-1]

            # start backtracking: leaf or visited
            if is_leaf(node) or is_children_visited(node):
                node = stack.pop()  # visit for real
                if mono[-1] is node:
                    mono.pop()
                if not mono:
                    break
                if mono[-1].val <= node.val:
                    result += 1
                visited[id(node)] = True
            else:
                if node.left and not visited[id(node.left)]:
                    stack.append(node.left)
                if node.right and not visited[id(node.right)]:
                    stack.append(node.right)
                if mono[-1] is not node and node.val >= mono[-1].val:
                    mono.append(node)
        return result


if __name__ == "__main__":
    solution = Solution()
    root = array_to_tree([2, 1, 1, 3, None, 1, 5])
    answer = solution.goodNodes(root)
    print(f"The number of good nodes is {answer}")  # 3
