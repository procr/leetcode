# fast power
#
# n could be negative

class Solution(object):

	def myPow(self, x, n):
		"""
		:type x: float
		:type n: int
		:rtype: float
		"""
		res = 1
		absN = abs(n)
		while absN > 0:
			# odd
			if absN & 1:
				res *= x
			x *= x
			absN >>= 1

		return res if n >= 0 else 1/res;


sol = Solution()
print sol.myPow(34.00515,-3)