#include <iostream>
#include <vector>
#include <numeric>
#include <limits>

using namespace std;


int num[3];

int helper(int l, int r)
{
    int mid = (l + r) >> 1;
    int left = 0;
    int right = 0;

    for (int i = 0; i < 3; ++i) {

        if (num[i] == mid) {
            return mid;
        }

        if (l <= num[i] && num[i] <= mid - 1) {
            ++left;
        } else {
            ++right;
        }
    }

    if (left > 0 && right > 0) {
        return mid;
    } else if (left > 0){
        return helper(l, mid - 1);
    } else {
        return helper(mid + 1, r);
    }

    return -1;
}

int main() {
    int k;
    int res;

    cin >> k >> num[0] >> num[1] >> num[2];

    res = helper(1, (2 << k) - 1);

    cout << res << endl;
    
    return 0;

}
