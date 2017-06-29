from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        c1, c2 = Counter(nums), {}
        for key, val in c1.items():
            c2.setdefault(val,[]).append(key)
        for i in range(len(nums), -1, -1):
        	if i in c2:
        		ans += c2[i]
        		k -= len(c2[i])
        		if k < 0:
        			ans = ans[:k]
        			return ans
        		elif k == 0:
        			return ans

        return ans


sol = Solution()
print sol.topKFrequent([1,1,1,2,2,2,3,3,3,4,4,4,4], 2)       