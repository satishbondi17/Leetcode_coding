class Solution(object):
    def mergeKLists(self, lists):
        l = []
        
        # Traverse all linked lists
        for i in range(len(lists)):
            node = lists[i]
            while node:
                l.append(node.val)
                node = node.next
        
        # Sort values
        l.sort()
         # Create new linked list
        dummy = ListNode(0)
        current = dummy
        
        for val in l:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next
        
       