# Definition for singly-linked list.
class ListNode:
    val = 0
    next = None
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if None == l1:
            return l2
        if None == l2:
            return l1
        head = ListNode(-1)
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
            
        cur = head

        while l1 or l2:
            if None == l1:
                cur.next = l2
                return head
            if None == l2:
                cur.next = l1
                return head
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next                
            else:
                cur.next = l1
                l1 = l1.next               
            cur = cur.next

        return head

l1 = ListNode(5)
l2 = ListNode(1)
t = ListNode(2)
l2.next = t
t = ListNode(4)
l2.next.next = t

s = Solution()
head = s.mergeTwoLists(l1, l2)

while head:
    print head.val
    head = head.next
