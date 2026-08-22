# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if root is None:
            return None
        if root == p or root == q:
            return root
        leftlca = self.lowestCommonAncestor(root.left,p,q)
        rightlca = self.lowestCommonAncestor(root.right,p,q)

        if leftlca is not None and rightlca is not None:
            return root
        elif leftlca is not None:
            return leftlca
        else:
            return rightlca
        