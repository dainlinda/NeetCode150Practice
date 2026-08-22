from utils.trees import TreeNode, array_to_tree, preorder_print_tree
from collections import deque
from typing import Optional


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        q = deque([root])
        result = [str(root.val)]

        while q:
            node = q.popleft()
            if node is not None:
                q.append(node.left)
                q.append(node.right)
                if node.left is not None:
                    result.append(str(node.left.val))
                else:
                    result.append("N")
                if node.right is not None:
                    result.append(str(node.right.val))
                else:
                    result.append("N")
        return ",".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        # string to list
        array_tree = data.split(",")
        n = len(array_tree)
        root = TreeNode(int(array_tree[0]))

        q = deque([root])
        i = 1
        while q:
            node = q.popleft()

            # left
            if i < n and array_tree[i] != "N":
                node.left = TreeNode(int(array_tree[i]))
                q.append(node.left)
            i += 1

            # right
            if i < n and array_tree[i] != "N":
                node.right = TreeNode(int(array_tree[i]))
                q.append(node.right)
            i += 1
        return root


if __name__ == "__main__":
    c = Codec()
    root = array_to_tree([1, 2, 3, None, None, 4, 5])
    serialized = c.serialize(root)
    print(serialized)
    preorder_print_tree(c.deserialize(serialized))
