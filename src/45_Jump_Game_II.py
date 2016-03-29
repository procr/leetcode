'''

boundary: 当前势力范围的边界
remote: 下一个势力范围的最大边界
r: 跨过了几个势力范围
i: iterator


simplify this question:
get accross the least 'sphere of influence'

http://www.cnblogs.com/lichen782/p/leetcode_Jump_Game_II.html

O(n)

so beautiful code! 

'''




class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        boundary, remote, r = 0, 0, 0
        n = len(nums)

        for i in xrange(n):
        	# cross over a 'sphere of influence'
        	if i > boundary:
        		boundary = remote
        		r += 1
        	remote = max(remote, i + nums[i])

        return r






