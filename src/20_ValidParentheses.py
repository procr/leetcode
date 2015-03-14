class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if 0 == len(stack):
                    return False
                cc = stack.pop()
                if cc == '(' and c != ')':
                    return False
                if cc == '[' and c != ']':
                    return False
                if cc == '{' and c != '}':
                    return False
        if 0 != len(stack):
            return False        
        return True
                
