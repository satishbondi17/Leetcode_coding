# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return "No intersection"
        skipA,skipB=headA,headB
        while skipA!=skipB:
            skipA=skipA.next if skipA else headB
            skipB=skipB.next if skipB else headA
        return skipA



      
        