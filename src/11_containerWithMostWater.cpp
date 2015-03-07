class Solution {
public:
    int maxArea(vector<int> &height) 
    {
    	/*
    		贪心
			正确是因为：当前两边height[l], height[r]， 比较短的一条能匹配到的最远的一定是对方这一条,所以height比较短的这个点可以skip掉

    	*/

    	int l = 0;
    	int r = height.size() - 1;
    	int max = 0;

    	while (l < r)
    	{
    		int area = (r - l) * min(height[l], height[r]);
    		if (area > max) 
    			max = area;
    		if (height[l] < height[r])
    			l++;
    		else
    			r--;
    	}

    	return max;        
    }
};