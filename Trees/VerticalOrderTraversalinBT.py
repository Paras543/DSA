# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        mp = {}
        q = deque([(root,0,0)])
        while q:
            node,hd,dp = q.popleft()
            if hd not in mp:
                mp[hd] = []
            mp[hd].append((dp,node.val))
          
            if node.left:
                q.append((node.left,hd-1,dp+1))
            if node.right:
                q.append((node.right,hd+1,dp+1))
            
        ans = []
        for hd in sorted(mp):
            mp[hd].sort()
            ans.append([val for dp,val in mp[hd]])
        return ans


        