'''
str * str...
'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0': 
        	return '0'

        a = [ord(i) - 48 for i in num1[::-1]]
        b = [ord(i) - 48 for i in num2[::-1]]
        len_a = len(num1)
        len_b = len(num2)
        res = [0] * (len_a + len_b)

        for i in xrange(len_a):
        	for j in xrange(len_b):
        		res[i + j] += a[i] * b[j]
        		res[i + j + 1] += res[i + j] / 10
        		res[i + j] %= 10

        return ''.join([chr(48 + i) for i in res])[::-1].lstrip('0')



sol = Solution()
print sol.multiply('123', '456')
