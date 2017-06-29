#include <iostream>

using namespace std;

int zeroNum(int n){  
    int ret = 0;  
    int baseNum = 5;  
    while (n >= baseNum)  
    {  
        ret += n/baseNum;  
        baseNum *= 5;  
    }  
    return ret;  
}  

int main() {
    int x;
    int y;
    while(cin >> x) {
        y = 1;
        int upper = y;
        int lower = 0;
        int n = 0;
        int ans = 0;

        while (1) {
            n = zeroNum(y);
            if (n < x) {
                lower = y;
                upper = upper << 1;
                y = upper;
            } else {
                break;
            }
        }

         
        while (1) {
            y = (lower + upper) / 2;
            n = zeroNum(y);

            if (lower == upper || lower == upper -1) {
                int n1 = zeroNum(lower);
                int n2 = zeroNum(upper);
                if (n1 == x) {
                    ans = lower;
                } else if (n2 == x) {
                    ans = upper;
                } else {
                    ans = -1;
                }
                break;
            }

            if (n < x) {
                lower = y;
            } else if (n >= x) {
                upper = y;
            } 
        }

        cout << ans << endl;
    }

    return 0;
}
