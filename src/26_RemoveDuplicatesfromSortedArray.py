class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
    	temp = None    	
    	i = 0
    	cur = 0

        while True:
        	if i == len(A):
        		break        	
        	if temp != A[i]:        		
        		temp = A[i]
        		A[cur] = A[i]
        		cur += 1

        	# del A[i] is not allowed
        	i += 1

        return cur

A = [1,1,1]
s = Solution()
print s.removeDuplicates(A)
print A