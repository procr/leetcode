class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        pos1 = -1
        pos2 = n -1
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pos1 = i - 1
                break

        if pos1 >= 0:
            for i in range(n - 1, pos1, -1):
                if nums[i] > nums[pos1]:
                    temp = nums[i]
                    nums[i] = nums[pos1]
                    nums[pos1] = temp
                    break


        pos1 += 1
        while pos1 < pos2:
            temp = nums[pos1]
            nums[pos1] = nums[pos2]
            nums[pos2] = temp
            pos1 += 1
            pos2 -= 1


sol = Solution()
#nums = [7, 8, 6, 9, 8, 7, 2]
nums = [3, 2, 1]
print nums
sol.nextPermutation(nums)
print nums

        
