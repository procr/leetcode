class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        tmp = 0
        for num in nums:
            if num == 1:
                tmp += 1
            else:
                tmp = 0
            if tmp > ans:
                ans = tmp

        return ans


sol = Solution()
print sol.findMaxConsecutiveOnes([1,1,0,0,1,1,1,1,0,1])
