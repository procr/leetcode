class Solution {
public:
	//string reverse
	char *strrev(char* s)
	{
		/* h指向s的头部 */  
	    char* h = s;      
	    char* t = s;  
	    char ch;  
	  
	    /* t指向s的尾部 */  
	    while(*t++){}
	    t--;    /* 与t++抵消 */  
	    t--;    /* 回跳过结束符'\0' */  
	  
	    /* 当h和t未重合时，交换它们所指向的字符 */  
	    while(h < t)  
	    {  
	        ch = *h;  
	        *h++ = *t;    /* h向尾部移动 */  
	        *t-- = ch;    /* t向头部移动 */  
	    }
	    return s;
	}

    int reverse(int x) {
    	bool neg = 0;
    	char *s =  new char(25);
    	int fac = 1;
    	if (x < 0)
    	{
    		neg = 1;
    		x = x * -1;
    	}
    	else if (x == 0)
    	{
    		return 0;
    	}

    	// How many zeros in the last bits
    	while (x % (fac * 10) == 0)
    		fac *= 10;

        sprintf(s, " %d" , x);
        s = strrev(s);
        int num = atoi(s); // answer candidate

        memset(s, 0, 25 * sizeof(char));
		sprintf(s, " %d" , num);
        s = strrev(s);
        int xx = atoi(s) * fac; // reverse again to see if equal

        if (xx != x) // overflowed
        	num = 0;
        else if (neg)
    		num *= -1;

    	delete s;
	    return num;
	}
};
