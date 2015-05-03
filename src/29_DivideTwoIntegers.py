class Solution:
    # 位运算
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        sign = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)  
        a, b = abs(dividend), abs(divisor)
        ret = 0
        base = [0] * 32

        bb = b
        i = 0
        while a >= bb:
            base[i] = bb
            i += 1
            bb <<= 1

        i -= 1

        while i >= 0:
            if a >= base[i]:
                a -= base[i]
                ret += 1 << i
                
            i -= 1
            
        if sign:
            ret = -ret

        return min(max(-2147483648, ret), 2147483647)
