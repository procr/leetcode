
'''
12
34

upside down:

34
12

diagonal flip

31
42

'''


class Solution(object):
	def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		n = len(matrix)
		if n < 2:
			return

		# upside down
		for i in xrange(n / 2):
			for j in xrange(n):
				matrix[i][j] ^= matrix[n - i - 1][j]
				matrix[n - i - 1][j] ^= matrix[i][j]
				matrix[i][j] ^= matrix[n - i - 1][j]

		# diagonal flip
		for i in xrange(n):
			for j in xrange(i + 1, n):
				matrix[i][j] ^= matrix[j][i]
				matrix[j][i] ^= matrix[i][j]
				matrix[i][j] ^= matrix[j][i]


sol = Solution()
matrix = [[1,2],[3,4]]
print matrix
sol.rotate(matrix)
print matrix