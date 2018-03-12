# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return 
        
        start = dum = ListNode(0)
        dum.next = head
        
        while dum.next:
            if dum.next.val == val:
                dum.next = dum.next.next
            else:
                dum = dum.next 
                
        return start.next
