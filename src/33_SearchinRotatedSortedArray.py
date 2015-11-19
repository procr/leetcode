class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # the problem says it only rotates once??????
        # since it is monotonic increasing, so [3 4 5 6 7 0 1 2] only the shape with 2 slopes will appear

        # binary search............

        n = len(nums)
        l = 0
        r = n
        cur = (l + r) / 2
        
        in_right = (target < nums[0])

        while nums[cur] != target:
            last = cur
            if in_right: # target in the right slope
                if nums[cur] > nums[0]: # current value in the left slope, search in the right
                    l = cur
                    cur = (cur + r) / 2
                else: # cur in right
                    if nums[cur] > target: # >target, search left
                        r = cur
                        cur = (cur + l) / 2
                    else: # <target, search right
                        l = cur
                        cur = (cur + r) / 2
            else: # target in left slope
                if nums[cur] < nums[0]: #  cur in right, search left
                    r = cur
                    cur = (cur + l) / 2
                else: # cur in left
                    if nums[cur] > target: # >target, search left
                        r = cur
                        cur = (cur + l) / 2
                    else: # <target, search right
                        l = cur
                        cur = (cur + r) / 2

            if last == cur:
                cur = -1
                break


        return cur
                     


sol = Solution()
#nums = [3,4,5,6,7,0,1,2]
nums = [1]
target = 0
print sol.search(nums, target)
