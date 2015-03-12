class Solution {
public:
    int threeSumClosest(vector<int> &num, int target) 
	{
		/*
			������ʽ��3sumһģһ��
		*/
        std::sort(num.begin(), num.end());
		int len = num.size();
		int min = INT_MAX;
		int ans;
		
		for (int i = 0; i < len; i++)
		{
			int l = i + 1;
			int r = len - 1;
			while (l < r)
			{
				int sum = num[i] + num[l] + num[r];
				if (target == sum)
					return sum;				
				else if (target < sum)
				{
					if (abs(sum - target) < min)
					{
						min = abs(sum - target);
						ans = sum;
					}
					r--;
				}
				else
				{
					if (abs(sum - target) < min)
					{
						min = abs(sum - target);
						ans = sum;
					}
					l++;
				}
					
			}			
		}
		return ans;
    }
};