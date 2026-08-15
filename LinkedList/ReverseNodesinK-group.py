# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        count = 0
        temp = head
        while count < k:
            if temp == None:
                return head

            temp = temp.next

            count += 1

        prev = self.reverseKGroup(temp,k)
        count = 0

        temp = head
        while count < k:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        
            count += 1
            

        return prev
