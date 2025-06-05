# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        current = head
        li = []
        while current:
            li.append(current.val)
            current = current.next
        
        li.sort()
        current = head
        for val in li:
            current.val = val
            current = current.next
        return head
            