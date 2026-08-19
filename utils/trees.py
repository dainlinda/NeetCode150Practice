from collections import deque


# Definition for a binary tree node, as provided in LeetCode problem
# starter code (used throughout the NeetCode 150 practice set).
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Claude-generated helper function
def array_to_tree(arr: list[int | None]) -> TreeNode | None:
    """Function to change a list form to a tree form

    Args:
        arr (List[int]): an array form of a binary tree following level order

    Returns:
        TreeNode | None : a tree form of a binary tree
    """
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    q = deque([root])

    i, n = 1, len(arr)

    while q and i < n:
        node = q.popleft()

        # left
        if i < n and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        # right
        if i < n and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root
