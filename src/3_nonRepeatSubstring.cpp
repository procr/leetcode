class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLen = 0;
        int curLen = 0;
        int start = 0;
        map<char, int> mm;
        for (int i = 0; i < s.size(); i++)
        {
            if (mm.find(s[i]) == mm.end())
            {
                curLen++;
                mm[s[i]] = i;
            }
            else
            {
            	if (mm[s[i]] < start)
            	{
            		curLen++;
            	}
            	else
            	{
                	if (curLen > maxLen)
                    	maxLen = curLen;
                	curLen = i - mm[s[i]];
                	start = mm[s[i]] + 1;
                }
                mm[s[i]] = i;
            }
        }
        if (curLen > maxLen)
            maxLen = curLen;
        return maxLen;
    }
};
