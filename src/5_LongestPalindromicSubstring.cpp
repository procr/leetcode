class Solution {
public:
	/*
		My method is DP
		There is another method called: Manacher
		See: http://www.cnblogs.com/tenosdoit/p/3675788.html
	*/
    string longestPalindrome(string s) {
        const int len = s.size();
        bool dp[len][len];
        int maxLen = 1;
        int left = 0;
        memset(dp, 0, sizeof(dp));

        dp[len - 1][len - 1] = 1;
        for (int i = 0; i < len - 1; i++)
        {
            dp[i][i] = 1;
            dp[i][i + 1] = (s[i] == s[i + 1]);
            if (dp[i][i + 1])
            {
                maxLen = 2;
                left = i;
            }
        }
        for (int k = 3; k <= len; k ++) // for each length
        {
            for (int i = 0; i < len; i++)
            {
                int j = i + k - 1;
                if (j >= len)
                    break;
                dp[i][j] = (s[i] == s[j]) && (dp[i + 1][j - 1]);
                if (dp[i][j] && k > maxLen)
                {
                    maxLen = k;
                    left = i;
                }
            }
        }
        return s.substr(left, maxLen);
    }
};
