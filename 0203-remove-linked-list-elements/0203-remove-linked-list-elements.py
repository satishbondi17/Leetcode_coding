# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        prev, curr = None, head
        while curr:
            if curr.val == val:  # cases 1-3
                if prev:  # cases 1-2
                    prev.next = curr.next
                else:  # case 3
                    head = curr.next
                curr = curr.next  # for all cases
            else:  # case 4
                prev, curr = curr, curr.next
        return head