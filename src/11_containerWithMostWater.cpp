class Solution {
public:
    int maxArea(vector<int> &height) 
    {
    	/*
    		贪心
			正确是因为：当前两边height[l], height[r]， 比较短的一条能匹配到的最远的一定是对方这一条,所以height比较短的这个点可以skip掉

            当从两边向中间考虑时，乘水的面积是由（两端较小的高度）×（两个板之间的宽度）决定的。

            假定初始的盛水面积为ans=0，lh为左边的高度，rh为右边的高度，如果lh < rh, 则向右运动，寻找第一个比当前lh大的左节点。同理，如果lh > rh，则向左运动，寻找第一个比当前rh大的右节点。

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