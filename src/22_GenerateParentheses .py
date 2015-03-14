class Solution:
    def helper(self, remains1, remains2, res, tmp):
        if 0 == remains2:
            res.append(tmp)
            return
        
        if remains1 == remains2:
            self.helper(remains1 - 1, remains2, res, tmp + '(')
        else:
            if remains1 > 0:
                self.helper(remains1 - 1, remains2, res, tmp + '(')
            self.helper(remains1, remains2 - 1, res, tmp + ')')
                
            

    
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        res = []

        self.helper(n, n, res, "")

        return res

s = Solution()
print s.generateParenthesis(3)
