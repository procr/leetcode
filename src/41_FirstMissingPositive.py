class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # tricky method! but nice

        n = len(nums)

        for i in xrange(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in xrange(n):
            idx = abs(nums[i])
            if idx <= n:
                nums[idx - 1] = -abs(nums[idx - 1])

        for i in xrange(n):
            if nums[i] > 0:
                return i + 1

        return n + 1


sol = Solution()
nums = [3,4,-1,1]
print sol.firstMissingPositive(nums)

