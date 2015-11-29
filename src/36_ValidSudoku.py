class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = {}
        columns = {}
        boxes = {}

        for i in xrange(9):
            rows[i] = set()
            columns[i] = set()
            boxes[i] = set()

        for i in xrange(9):
            for j in xrange(9):
                c = board[i][j]
                if c == ".":
                    continue
                k = i // 3 + j // 3 * 3
                if c in rows[i] or c in columns[j] or c in boxes[k]:
                    return False
                rows[i].add(c)
                columns[j].add(c)
                boxes[k].add(c)

        return True


sol = Solution()
#print sol.isValidSudoku([..])


