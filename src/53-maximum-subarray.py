class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        the key point is to compare with 0
        
        """
        
        n = len(nums)
        res = nums[0]
        temp = 0

        for i in xrange(n):
            temp = nums[i] + (temp > 0 and temp) or 0

            if temp > res:
                res = temp

        return res 

        


a = [-2,1,1,4,-1,2,1,-5,4]
sol = Solution()
print sol.maxSubArray(a)
