class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        B = filter(lambda x : x != elem, A)
        for i in range(len(B)):
        	A[i] = B[i]

        return len(B)
