class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_dist = 0
        for i, j in enumerate(nums):
            if i > max_dist:
                return False
            if i + j > max_dist:
                max_dist = i + j

        return True