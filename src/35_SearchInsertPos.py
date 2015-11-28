class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = 0
        r = len(nums)
        if r == 0:
            return 0
        if target < nums[l]:
            return 0
        if target > nums[r - 1]:
            return r
        cur = (l + r) / 2
        while True:
            last = cur
            if target == nums[cur]:
                break
            elif target > nums[cur]:
                l = cur
                cur = (l + r) / 2
            else:
                r = cur
                cur = (l + r) / 2

            if last == cur:
                cur += 1
                break

        return cur



sol = Solution()
nums = [1,3,4,6]
target = 2
print sol.searchInsert(nums, target)       
