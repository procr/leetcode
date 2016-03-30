'''
permutation

in swap way

'''

import math
import random
class Solution(object):

	# random way, but it is tricky
	def permute_tricky(self, nums):
	    res = []
	    while len(res) < math.factorial(len(nums)):
	        while nums in res:
	            random.shuffle(nums)
	        res.append(nums[:])
	    return res

	# this is the swap method, swap last element
	# beautiful
	def permute(self, nums):
		"""
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
		n = len(nums)
		if n <= 1: return [nums]
		r = []
		for i in xrange(n):  
		    s = nums[: i] + nums[i + 1 :]  
		    p = self.permute(s)  
		    for x in p:  
		        r.append(nums[i : i + 1] + x)  
		return r  
       

sol = Solution()
print sol.permute([1,2,3,4])

