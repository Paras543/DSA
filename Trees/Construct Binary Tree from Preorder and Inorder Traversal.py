# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def search(self,inoder,left,right,val):
        for i in range(left,right+1):
            if inoder[i] == val:
                return i
        return -1
    def helper(self,preorder,inoder,preidx,left,right):
        if left > right:
            return None
        root = TreeNode(preorder[self.preidx]) # type: ignore
        Inidx = self.search(inoder,left,right,preorder[self.preidx])
        self.preidx += 1
        root.left = self.helper(preorder,inoder,preidx,left,Inidx-1)
        root.right = self.helper(preorder,inoder,preidx,Inidx+1,right)
        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.preidx = 0
        return self.helper(preorder,inorder,self.preidx,0,len(inorder)-1)