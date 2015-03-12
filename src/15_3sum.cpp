class Solution 
{
public:	
    vector<vector<int>> threeSum(vector<int> &num) 
	{
		
		/*
			����
			�ѵ�һ������target��Ȼ����β����ָ��������תΪ2sum���⣨���������2sum���⣬���Բ�Ҫ��map��
		*/
	
		std::sort(num.begin(), num.end());
		int len = num.size();
		vector<vector<int> > res;
		for (int i = 0; i < len; i++)
		{
			int l = i + 1;
			int r = len - 1;
			while (l < r)
			{
				if (0 == num[i] + num[l] + num[r])
				{
					vector<int> sol;
					sol.push_back(num[i]);
					sol.push_back(num[l]);
					sol.push_back(num[r]);
					res.push_back(sol);
					l++;
					r--;
					
					//avoid duplicate
					while(l < r && num[l] == num[l - 1]) l++;
					while(l < r && num[r] == num[r + 1]) r++;					
				}
				else if (0 < num[i] + num[l] + num[r])
					r--;
				else
					l++;				
			}
			
			//avoid duplicate
			while(i < len - 1 && num[i] == num[i + 1])
				i++;  
		}
		return res;        
    }
};