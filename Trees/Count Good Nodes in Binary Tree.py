# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = [0]
        def dfs(node,max_far):
            
            if node is None:
                return 
            if node.val >= max_far:
                count[0] += 1
            max_far = max(max_far,node.val)
            dfs(node.left,max_far)
            dfs(node.right,max_far)
        dfs(root,root.val)

        return count[0]



        