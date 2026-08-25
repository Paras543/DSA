# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        prev_order = [0]

        def helper(root):

            if root is None:
                return -1

            if root.left:
                left_ans = helper(root.left)

                if left_ans != -1:
                    return left_ans

            prev_order[0] += 1

            if prev_order[0] == k:
                return root.val

            if root.right:
                right_ans = helper(root.right)

                if right_ans != -1:
                    return right_ans

            return -1

        return helper(root)


        