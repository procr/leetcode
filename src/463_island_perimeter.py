class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = 0
        if h > 0:
            w = len(grid[0])

        ans = 0

        for i in xrange(h):
            for j in xrange(w):
                if grid[i][j] == 1:
                    if j == 0 or grid[i][j - 1] == 0:
                        ans += 1
                    if i == 0 or grid[i - 1][j] == 0:
                        ans += 1
                    if j == w - 1 or grid[i][j + 1] == 0:
                        ans += 1
                    if i == h - 1 or grid[i + 1][j] == 0:
                        ans += 1

        return ans

grid = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
sol = Solution()
print sol.islandPerimeter(grid)
