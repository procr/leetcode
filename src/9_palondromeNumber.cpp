class Solution {
public:
    bool isPalindrome(int x) {
        int digits[20];
        if (x < 0)
            return false;
        int len = 0;
        while (x / 10 || x % 10)
        {
            digits[len++] = x % 10;
            x /= 10;
        }
        int i, j;
        if (len & 1) //odd
        {
            i = len / 2 - 1;
            j = len / 2 + 1;
        }
        else // even
        {
            i = len / 2 - 1;
            j = len / 2; 
        }
        while (i >= 0 && j < len)
        {
            if (digits[i--] == digits[j++])
                continue;
            return false;
        }
        return true; 
    }
};
