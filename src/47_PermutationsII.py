class Solution(object):

	# methid one:
	# sorted first and then add 2 lines of code which differ from permutation I
	def permuteUnique(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		return self.permuteUnique_helper(sorted(nums))

	def permuteUnique_helper(self, nums):
		n = len(nums)
		if n <= 1: return [nums]
		r = []
		for i in xrange(n):

			# the different part from permutation I
			if i > 0 and nums[i - 1] == nums[i]:
				continue

			s = nums[: i] + nums[i + 1 :]
			p = self.permuteUnique_helper(s)  
			for x in p:  
					r.append(nums[i : i + 1] + x)  
		return r  



	# another one line method: 
	#[] or [[]] will return [[]]
	#[].index(i) will return the first index of value i, [1,2,2,3].index(2) --> 1
	def permuteUnique_2(self, nums):
		return [[n] + p for n in set(nums) for p in self.permuteUnique_2(nums[:nums.index(n)] + nums[nums.index(n) + 1:])] or [[]]


sol = Solution()
print sol.permuteUnique_2([3,3,1,2,3,2,3,1])
