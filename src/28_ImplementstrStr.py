class Solution:

	# KMP!

	# @param needle, a string
    # @return a list
	def calcNext(self, needle):
		m = len(needle)
		next = [-1 for i in range(m)]
		next[0] = 0
		k = 0
		for i in range(1, m):
			while k > 0 and needle[k] != needle[i]:
				k = next[k - 1]
			if needle[k] == needle[i]:
				k += 1
			next[i] = k

		return next


    # @param haystack, a string
    # @param needle, a string
    # @return an integer
	def strStr(self, haystack, needle):
		n = len(haystack)
		m = len(needle)
		if 0 == m:
			return 0
		next = self.calcNext(needle)
		i = 0
		j = 0
		while i + m - j <= n:
			if haystack[i] == needle[j]:				
				if j == m - 1:
					return i - m + 1
				i += 1
				j += 1
			elif j > 0:
				j = next[j - 1]
			else:
				i += 1

		return -1


haystack = "dddabcdabaabcdabd"
needle = "abcdabd"
s = Solution()
print s.calcNext(needle)
print s.strStr(haystack, needle)