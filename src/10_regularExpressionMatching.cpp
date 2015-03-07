class Solution {
public:
    bool isMatch(const char *s, const char *p) 
    {
    	/*
    		三个注意点：
    			1. p 要完全而且不多不少刚好cover s.

    			2. *可以代表0次

    			3. ”.*“ == ...... == 任意的字符组合 ！= 先把.翻译成一个字符然后再*扩展

    	*/

    	// method 1: 递归

    	/*
    	if (0 == *p)
    		return 0 == *s;

    	if ('*' != *(p + 1))
    	{
    		if (*s == *p || (*p == '.' && 0 != *s))
    			return isMatch(s + 1, p + 1);
    		return false;
    	}
    	else
    	{
    		while (*s == *p || (*p == '.' && 0 != *s))
    		{
    			 if (isMatch(s, p + 2))
    			 	return true;
    			 s++;
    		}
    		return isMatch(s, p + 2);
    	}

        */

    	//method 2: DP

    	int m = strlen(s);
    	int n = strlen(p);

    	bool f[m + 1][n + 1]; //f[i + 1][j + 1]表示s前i位和p前j位是否能匹配

    	f[0][0] = true;

    	for (int i = 0; i < m; i++)
    		f[i + 1][0] = false;

    	for (int j = 0; j < n; j++)
    		f[0][j + 1] = ('*' == p[j]) && f[0][j - 1];

    	for (int i = 0; i < m; i++)
    		for (int j = 0; j < n; j++)
    			if ('*' != p[j])
    				f[i + 1][j + 1] = f[i][j] && ('.' == p[j] || s[i] == p[j]);
    			else
    				f[i + 1][j + 1] = f[i + 1][j - 1] ||	// take none
    									f[i + 1][j] ||		// take one 
    									(f[i][j + 1] && ('.' == p[j - 1] || s[i] == p[j - 1]));		// take 2 or more
    	return f[m][n];
    }
};