class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 1:
            return str(1)

        # recursion here...
        s = self.countAndSay(n - 1)

        cur = s[0]
        cnt = 0
        temp = ""
        for i in xrange(len(s)):
            if s[i] == cur:
                cnt += 1
            else:
                temp += (str(cnt) + cur)
                cur = s[i]
                cnt = 1
        temp += (str(cnt) + cur)
        return temp


sol = Solution()
print sol.countAndSay(5)
