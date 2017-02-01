class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        mask = num
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16
        return num ^ mask



sol = Solution()
print bin(sol.findComplement(0b10111))
