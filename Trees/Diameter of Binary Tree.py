# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = 0
    def height(self,root):
        if root is None:
            return 0
        leftht = self.height(root.left)
        rightht = self.height(root.right)

        self.ans = max(leftht+rightht,self.ans)
        return max(leftht,rightht) + 1
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.height(root)
        return self.ans