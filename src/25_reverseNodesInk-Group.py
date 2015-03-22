# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
    	if 1 == k:
    		return head
    	dummy = ListNode(0)
    	dummy.next = head
    	cur = head
    	n = 0
        while cur:
        	n = n + 1
        	cur = cur.next
        n = n / k 
        # n groups

        cur = dummy
        for i in range(n):
        	lastGroupTail = cur
        	first = lastGroupTail.next        	
        	last = ListNode(0)
        	cur = first
        	for j in range(k):        		        		
        		next = cur.next
        		if 0 == j:
        			last = cur
        			cur = next
        			continue
        		if k - 1 == j:
        			cur.next = last
        			lastGroupTail.next = cur
        			cur = first
        			cur.next = next
        			break
        		cur.next = last
        		last = cur
        		cur = next

        return dummy.next






