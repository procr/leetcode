import string

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.helper(board, 0, 0)

    def helper(self, board, i, j):
        if i == 9:
            return True
        if j == 9:
            return self.helper(board, i + 1, 0)

        if board[i][j] == ".":
            base = ord("1")
            for k in xrange(9):
                board[i][j] = chr(base + k)
                if self.isValid(board, i , j):
                    if self.helper(board, i, j + 1):
                        return True
                board[i][j] = "."
        else:
            return self.helper(board, i, j + 1)

        return False

    def isValid(self, board, i, j):
        for k in xrange(9):
            if k != j and board[i][j] == board[i][k]:
                return False
            if k != i and board[i][j] == board[k][j]:
                return False
        
        bi = i // 3 * 3
        bj = j // 3 * 3
        for r in xrange(bi, bi + 3):
            for c in xrange(bj, bj + 3):
                if (r != i and c != j):
                    if board[r][c] == board[i][j]:
                        return False

        return True

#print string.lowercase[:]
#print chr(ord("1"))

sol = Solution()
board = [["." for i in xrange(9)] for i in xrange(9)]
sol.solveSudoku(board)
print board


