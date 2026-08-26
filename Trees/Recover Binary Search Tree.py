# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.prev = None
        self.first = None
        self.second = None
    def inorder(self,root):
        if root is None:
            return None
        self.inorder(root.left)
        if self.prev is not None and root.val < self.prev.val:
            if self.first is  None:
                self.first = self.prev
            self.second = root

        self.prev = root
        self.inorder(root.right)

    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        self.inorder(root)
        self.first.val,self.second.val = self.second.val,self.first.val
