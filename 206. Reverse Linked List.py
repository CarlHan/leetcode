# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        pre = None       ##注意此处将第一个pre设置为None，不要设置为ListNode(x), 否则会多出一个结点
        
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre
