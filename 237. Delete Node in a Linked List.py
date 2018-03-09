# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
##这里注意sin-list，所以拿不到之前的元素指向的指针，只能拿到node.next(pointer),把value复制过来，将当前的pointer跳过下一个就ok了
