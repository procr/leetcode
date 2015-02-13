class Solution {
	/*
		Z字型字符串遍历，坐标转换。。。数学题。。。面试应该不会这么问吧。。。
	*/
public:
    string convert(string s, int nRows) 
    {
        if (nRows <= 1)
            return s;

        int len = s.size();
        int lettersPerZig = 2 * nRows - 2;
        string result;

        for(int i = 0; i < nRows; i++)
        {
            for(int j = 0, idx = i; 
            	idx < len; 
            	j++, idx = lettersPerZig * j + i)
            {
                result.append(1, s[idx]);
                if (i > 0 && i < nRows - 1)
                {
                    idx = lettersPerZig * j + 2 * nRows - 2 - i;
                    if (idx < len)
                        result.append(1, s[idx]);
                }
            }
        }
        return result; 
    }
};
