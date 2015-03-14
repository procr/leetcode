# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        ll = head
        l = head
        r = head
        while r :            
            if n > 0:
                r = r.next
                n = n - 1
            else:
                r = r.next
                ll = l
                l = l.next
                
        if l == head:
            head = head.next
        else:
            ll.next = l.next
        return head
                
            
        
