class Solution {
public:
    int atoi(string str) {
        set<char> validChar;
		validChar.insert('+');
		validChar.insert('-');
		validChar.insert('0');
		validChar.insert('1');
		validChar.insert('2');
		validChar.insert('3');
		validChar.insert('4');
		validChar.insert('5');
		validChar.insert('6');
		validChar.insert('7');
		validChar.insert('8');
		validChar.insert('9');
		
		int l = 0, r = -1;
		int len = str.length();
		int positive = 1;
		int ans = 0;
		
		for(int i = 0; i < len; i++)
		{
			if (str[i] == ' ' || str[i] == '\t')
			{
				l = i;
				continue;
			}
			break;			
		}
		
		if (str[l] == ' ' || str[l] == '\t')
		{
			if (l + 1 < len)
				l += 1;
			else 
				return 0;
		}
		
		for(int i = l; i < len; i++)
		{
			set<char>::iterator it;
            it = validChar.find(str[i]);
            if(it != validChar.end())
			{
				r = i;
				if (*it == '-' || *it == '+')
				{
					validChar.erase('-');
					validChar.erase('+');
				}
				continue;
			}
			break;
		}
		
		if (str[l] == '-')
		{
			positive = -1;
			l++;
		}
		else if (str[l] == '+')
		{
			l++;
		}
		
		for (int i = l; i <= r; i++)
		{
			if (ans > (INT_MAX - (str[i] - '0')) / 10) // overflow
			{
				if(positive == 1)
					return INT_MAX;
				else
					return INT_MIN; 
			}
			ans = ans * 10 + (str[i] - '0');
		}
		
		return positive * ans;
		
    }
};