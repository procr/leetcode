class Solution(object):
	def solveNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""

		def dfs(board, row):
			if row == n:
				r = ['.' * board[i] + 'Q' + '.' * (n - board[i] - 1) for i in xrange(n)]
				res.append(r)
			else:
				for i in all_num - set(board):
					if all(row - j != abs(i - board[j]) for j in xrange(row)):
						board[row] = i
						dfs(board, row + 1)
						board[row] = -1

		res = []
		all_num = {i for i in xrange(n)}
		dfs([-1] * n, 0)

		return res

sol = Solution()
print sol.solveNQueens(4)