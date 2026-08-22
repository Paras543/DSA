from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return None
        max_width = 0
        queue = deque([(root,0)])
        while queue:
            level_length = len(queue)
            first_index = queue[0][1]

            for i in range(level_length):
                node,index = queue.popleft()

                index = index - first_index
                if node.left:
                    queue.append((node.left,2*index))
                if node.right:
                    queue.append((node.right,2*index+1))

                if i == level_length - 1:
                    last_index = index
            width = last_index + 1
            max_width = max(max_width,width)
        return max_width


## IN this you know the logic just understand the code once more 