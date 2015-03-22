# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 假设一共是k个list
# 构建一个大小为k的堆，最开始把k个list的第一个元素加入heap
# 然后弹出最小的，加入到答案的list
# 然后把弹出元素所在的list的下一个元素push进入heap
# 利用heapq数据结构
#

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = []
        for head in lists:
        	if head:
        		heap.append((head.val, head))
        heapq.heapify(heap)
        h = ListNode(0)
        cur = h
        while heap:
        	(val, node) = heapq.heappop(heap)
        	cur.next = ListNode(val)
        	cur = cur.next
        	if node.next:
        		heapq.heappush(heap, (node.next.val, node.next))

        return h.next
