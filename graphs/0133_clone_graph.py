from typing import Optional
from utils.graphs import ADJNode, print_adj_graph


class Solution:
    def cloneGraph(self, node: Optional["ADJNode"]) -> Optional["ADJNode"]:
        if not node:
            return None
        copies = {id(node): ADJNode(node.val, [])}
        stack = [node]

        while stack:
            nd = stack.pop()
            new_nd = copies[id(nd)]

            for neighbor in nd.neighbors:
                if id(neighbor) not in copies:  # create a new
                    copies[id(neighbor)] = ADJNode(neighbor.val, [])
                    stack.append(neighbor)
                new_nd.neighbors.append(copies[id(neighbor)])
        return copies[id(node)]


if __name__ == "__main__":
    sol = Solution()
    A, B, C = ADJNode(1, []), ADJNode(2, []), ADJNode(3, [])
    A.neighbors.append(B)
    B.neighbors.append(A)
    B.neighbors.append(C)
    C.neighbors.append(B)

    copied_graph = sol.cloneGraph(A)
    print_adj_graph(copied_graph)
