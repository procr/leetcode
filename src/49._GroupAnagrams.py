'''
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]


bisect insort_left

'''

class Solution(object):
	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""

		import bisect

		def hashFunc(s):
			# represent hash value of a..z
			primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
			hash = 1
			for c in s:
				hash *= primes[ord(c) - ord('a')]
			return hash

		res = {}
		for s in strs:
			h = hashFunc(s)
			if h not in res:
				res[h] = [s]
			else:
				bisect.insort_left(res[h], s)

		return res.values()

sol = Solution()
print sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])