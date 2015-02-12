class Solution {
public:
    int findKth(int A[], int m, int B[], int n, int k) // idx: 0, 1, 2, ... , k, ... find kth
    {
        if (m > n)
            return findKth(B, n, A, m, k);

        if (0 == m)
            return B[k];

        if (0 == k)
            return A[0] < B[0] ? A[0] : B[0];

        if (1 == m)
        {
        	if (A[0] < B[k - 1])
        		return B[k - 1];
        	else if (1 == n)
        		return A[0];
        	else if (A[0] < B[k])
        		return A[0];
        	else
        		return B[k];            
        }

        if (1 == k)
        {
        	if (A[0] > B[0])
        	{
        		if (A[0] > B[1])
        			return B[1];
        		else
        			return A[0];
        	}
        	else
        	{
        		if (B[0] > A[1])
        			return A[1];
        		else
        			return B[0];
        	}
        	
        }

        int mm = m - 1 < (k / 2) ? m - 1 : k / 2;
        int nn = k / 2;

        if (A[mm] < B[nn])
            return findKth(A + mm, m - mm, B, n, k - mm);
        else if (A[mm] > B[nn])
            return findKth(A, m, B + nn, n - nn, k - nn);
        else // ==
            return A[mm];


    }

    double findMedianSortedArrays(int A[], int m, int B[], int n) 
    {
        if ((m + n) & 1)        
            return findKth(A, m, B, n, (m + n) / 2);   
        else        
            return (findKth(A, m, B, n, (m + n) / 2 - 1) + findKth(A, m, B, n, (m + n) / 2)) / 2.0;
    }
};
