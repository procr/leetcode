class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # maybe because using floating.. so it is not that fast....


        #binary search...

        if len(nums) == 0:
            return [-1, -1]

        #===================================
        lb = target - 0.5 # left bound
        l = 0
        r = len(nums)
        cur1 = (l + r) / 2
        while True:
            last = cur1
            if nums[cur1] > lb:
                r = cur1
                cur1 = (l + r) / 2
            else:
                l = cur1
                cur1 = (l + r) / 2

            if last == cur1:
                if nums[cur1] == target:
                    break
                elif (cur1 + 1 < len(nums)) and (nums[cur1 + 1] == target):
                    cur1 += 1
                    break
                else:
                    return [-1, -1]

        #===================================
        rb = target + 0.5 # right bound
        l = 0
        r = len(nums)
        cur2 = (l + r) / 2
        while True:
            last = cur2
            if nums[cur2] > rb:
                r = cur2
                cur2 = (l + r) / 2
            else:
                l = cur2
                cur2 = (l + r) / 2

            if last == cur2:
                break

        return [cur1, cur2]


 
 
sol = Solution()
nums = [1,5,5,5,5,5,5,6]
target = 5
print sol.searchRange(nums, target)       
