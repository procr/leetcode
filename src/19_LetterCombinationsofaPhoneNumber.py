import string

class Solution:
        def helper(self, letters, res, digits, idx, tmp):                
                if idx == len(digits):
                        res.append(tmp)
                        return
                digit = string.atoi(digits[idx])
                cur = letters[digit - 2]
                for i in cur:
                        tmp = tmp + i                        
                        self.helper(letters, res, digits, idx + 1, tmp)
                        tmp = tmp[:len(tmp) - 1]
    
        # @return a list of strings, [s1, s2]
        def letterCombinations(self, digits):
                if 0 == len(digits):
                        return []
                letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
                res = []
                self.helper(letters, res, digits, 0, "")    
                return res
        
s = Solution()
print s.letterCombinations("23")
