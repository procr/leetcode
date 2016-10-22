class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        """
        n = len(matrix)
        m = 0
        if n > 0:
            m = len(matrix[0])
        t = m * n
        res = [0 for i in xrange(t)]

        x0 = 0
        y0 = 0
        x1 = n - 1
        y1 = m - 1

        i = 0

        while x0 <= x1 and y0 <= y1:
            x = x0
            y = y0
            res[i] = matrix[x][y]
            i = i + 1
            if y + 1 <= y1:
                y = y + 1
            elif x + 1 <= x1:
                x = x + 1
            

            while ((x != x0 or y != y0) and i < t):
                res[i] = matrix[x][y]
                i = i + 1
                if x == x0 and y != y1:
                    y = y + 1
                elif y == y1 and x != x1:
                    x = x + 1
                elif x == x1 and y != y0:
                    y = y - 1
                elif y == y0 and x != x0:
                    x = x - 1
                
                
                

            x0 = x0 + 1
            y0 = y0 + 1
            x1 = x1 - 1
            y1 = y1 - 1

        return res


#a = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
#a = [[3],[2]]
#a = [[6,9,7]]
a = [[7],[9],[6]]
sol = Solution()
print sol.spiralOrder(a)
