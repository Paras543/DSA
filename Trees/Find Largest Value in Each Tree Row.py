from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            max_val = float("-inf")
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                max_val = max(max_val,node.val)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(max_val)

            
            
        return result

        