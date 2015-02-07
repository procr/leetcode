class Solution 
{
public:
	/*
		用两重循环是最简单的办法，但是会超时。
		利用一个map来存曾经访问到的地方，下次如果碰到了的地方和上次的和加起来等于target，也就找到了。
	*/
    vector<int> twoSum(vector<int> &numbers, int target) 
    {
        vector<int> ans(2);
		map<int, int> mm;
        int n = numbers.size();
        for(int i = 0; i < n; i++)
        {
            if (mm.find(numbers[i]) == mm.end())
			{
				mm[target - numbers[i]] = i;
			}
			else
			{
				ans[0] = mm[numbers[i]] + 1;
				ans[1] = i + 1;
				return ans;
			}
        }
        return ans;
    }
};