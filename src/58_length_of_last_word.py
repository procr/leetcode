class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        s.split() is different from s.split(" ")
        when s = "1 "
        s.split() = ["1"]
        s.split(" ") = ["1", ""]
        ?????? fuck

        but you can't return len(s.split()[-1]),
        when s = ""  or "   "
        [-1] will out of range...
        ????? fuck 


        """
        split = s.split()
        return len(split[-1]) if split != [] else 0

sol = Solution()
print sol.lengthOfLastWord(" ")
