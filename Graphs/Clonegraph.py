"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        if not node:
            return None
        clones = {}

        def dfs(node):
            if node in clones:
                return clones[node]
            clone = Node(node.val) # type: ignore
            clones[node] = clone

            for neighbour in node.neighbors:
                clone.neighbors.append(dfs(neighbour))
            return clone

        return dfs(node)