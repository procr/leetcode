/**
* Definition for singly-linked list.
*     struct ListNode {
*     int val;
*     ListNode *next;
*     ListNode(int x) : val(x), next(NULL) {}
* };
*/

class Solution 
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) 
    {
        int carryBit = 0;
        ListNode *l = new ListNode(0);
        ListNode *ll1 = NULL;
        ListNode *ll2 = NULL;
        ListNode *cur = l;
        if (l1)
        {
            l->val += l1->val;
            ll1 = l1->next;
        }
        if (l2)
        {
            l->val += l2->val;
            ll2 = l2->next;
        }
        carryBit = l->val / 10;
        l->val = l->val % 10;
        while(ll1 || ll2)
        {
            ListNode *ll = new ListNode(carryBit);
            carryBit = 0;
            if (ll1)
            {
                ll->val += ll1->val;
                ll1 = ll1->next;
            }
            if (ll2)
            {
                ll->val += ll2->val;
                ll2 = ll2->next;
            }
            carryBit = ll->val / 10;
            ll->val = ll->val % 10;
            cur->next = ll;
            cur = ll;
        }

        if (carryBit)
        {
        	ListNode *ll = new ListNode(carryBit);
        	cur->next = ll;
            cur = ll;
        }
    	return l;
    } 
};

