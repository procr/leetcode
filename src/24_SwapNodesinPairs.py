# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
    	dummy = ListNode(0)
    	dummy.next = head    	
        fir = dummy
        sec = head
        if not sec:
        	return sec
        third = sec.next
        if not third:
        	return sec
        forth = third.next

        while True:
        	# 1 -> 2 -> 3 -> 4
        	fir.next = third
        	third.next = sec
        	sec.next = forth

        	# 1 -> 3 -> 2 ->4
        	fir = sec
        	sec = forth
        	if not sec:
        		return dummy.next
        	third = sec.next
        	if not third:
        		return dummy.next
        	forth = third.next
