class Solution(object):
    
    # purely stack...
    # O(n)
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0

        # idx represents the index of each character in 's'
        idx = [-1 for i in range(n)]

        # stack of parentheses
        stack = [' ' for i in range(n)]
        head = -1 

        ans = 0

        for i in range(n):
            if (s[i] == ')') and (head >= 0) and (stack[head] == '('):
                head -= 1
                cur = i - idx[head]
                if ans < cur:
                    ans = cur
            else: 
                head += 1
                stack[head] = s[i]
                idx[head] = i

        return ans



    # DP...
    # however....time limit exceeded
    # O(n^3)
    def longestValidParentheses_tle(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0

        # f[i][j] presents the longestValidParentheses between i and j
        f = [[0 for i in range(n)] for j in range(n)]

        for i in range(n - 1):
            if s[i] == '(' and s[i + 1] == ')':
                f[i][i + 1] = 2

        for l in range(3, n + 1):
            for i in range(n):
                j = i + l - 1
                if j < n:
                    for k in range(i, j, 1):
                        if (f[i][k] == k - i + 1) and (f[k + 1][j] == j - k): # chain them
                            f[i][j] = j - i + 1

                        else: # select one half
                            if f[i][k] > f[k + 1][j]: # left half
                                if f[i][k] > f[i][j]:
                                    f[i][j] = f[i][k]
                            else: # right half
                                if f[k + 1][j] > f[i][j]:
                                    f[i][j] = f[k + 1][j]


                        # wrap them
                        if (f[i + 1][j - 1] == j - i - 1) and s[i] == '(' and s[j] == ')':
                            f[i][j] = f[i + 1][j - 1] + 2 


        return f[0][n - 1]

sol = Solution()
s = "()(()"
print sol.longestValidParentheses(s)

