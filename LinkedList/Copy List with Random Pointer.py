"""
#Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        
        mp = {}
        newhead = Node(head.val)
        oldTemp = head.next
        newTemp = newhead
        mp[head] = newhead

        while oldTemp:
            copynode = Node(oldTemp.val)
            mp[oldTemp] = copynode
            newTemp.next = copynode
            oldTemp = oldTemp.next
            newTemp = newTemp.next
        
        oldTemp = head
        newTemp = newhead

        while oldTemp:
            if oldTemp.random:
                newTemp.random = mp[oldTemp.random]
            oldTemp = oldTemp.next
            newTemp = newTemp.next

        return newhead


        
## Revise this question 2 to 3 times