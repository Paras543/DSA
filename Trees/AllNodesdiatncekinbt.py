# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if root is None:
            return None
        parent = {}

        def build_parent(node,par= None):
            if node is None:
                return
            
            parent[node] = par
            build_parent(node.left,node)
            build_parent(node.right,node)
        build_parent(root)

        result = []
        visited_set = set()

        def dfs(node,distance):
            if node is None or node  in visited_set:
                return
            visited_set.add(node)
            if distance == k:
                result.append(node.val)
                return 
            dfs(node.left,distance+1)
            dfs(node.right,distance+1)
            dfs(parent[node],distance+1)
        dfs(target,0)
        return result


            

        