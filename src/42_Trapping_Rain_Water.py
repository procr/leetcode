'''
描述： 坐标上有很多高度不同的点，下一场雨，求出最多的积水量
和11题类似，不过这道题不是找到最合适的两个点组成一个容器。

解法一：有点点像动归，O(2*n)time, O(n)space
每一个坐标点f(i)有两个阶段的表示：
1. 首先从往右-->， 计算出以当前点i的，在左边最高点下能存储多少水量。
	如果碰到更高的点，那么更新最高高度，继续上面的步骤。
	f(i)此时记录的是：点i左边的最高高度（能够让它盛最多水）
2. 再从右往左<--，利用右边最高高度做第1步类似的事情
	f(i)此时记录的是：点i能够存储的最大水量。
	trap1中leftHeight数组即第一阶段的f，第二阶段的f其实不需要存了，直接累加到总数就好了

解法二：两个指针同时向内侧移动， O(n)time, O(1)space
当前左边高度f(0) = l， 右边高度f(n - 1) = r，选择比较矮的一方向内侧移动。
	举个例子，l<r，此时右方有r罩着，当前情况下，下一个节点(0< i < n -1)的高度f(i)只要比l还矮，
	那么他一定只能以存储到l这么高的水，这是瓶颈。
	所以每一次只要移动比较矮的一边，计算当前窗口下的水量。
'''

class Solution(object):
	# beats 36.98%
	def trap1(self, height):
		n = len(height)
		leftHeight= [0] * n
		maxHeight = 0
		for i in range(n):
			maxHeight = max(maxHeight, height[i])
			leftHeight[i] = maxHeight
		maxHeight = 0
		water = 0
		for i in range(n-1, -1, -1):
			maxHeight = max(maxHeight, height[i])
			water += min(maxHeight, leftHeight[i]) - height[i] #Note, this is always non-negative.
		return water

	# beats 52.66%
	def trap2(self, height):
		if (not height) or len(height) == 0:
			return 0
		l = 0
		r = len(height) - 1
		water = 0
		while l < r:
			m = min(height[l], height[r])
			if height[l] == m:
				l += 1
				while l < r and height[l] < m:
					water += m - height[l];  
					l += 1
			else:
				r -= 1  
				while l < r and height[r] < m:
					water += m - height[r]
					r -= 1

		return water;  


	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		#return self.trap1(height)
		return self.trap2(height)

sol = Solution()
print sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
        