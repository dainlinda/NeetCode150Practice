# Definition for a Node of a connected undirected graph
# Represented as an adjacency list
class ADJNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"node.val={self.val}, node.neighbors={[neighbor.val for neighbor in self.neighbors]}"


def print_adj_graph(root: ADJNode) -> None:
    stack = [root]
    visited = {id(root)}

    while stack:
        node = stack.pop()
        print(node)
        for neighbor in node.neighbors:
            if id(neighbor) not in visited:
                visited.add(id(neighbor))
                stack.append(neighbor)
