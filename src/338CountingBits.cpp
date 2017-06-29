#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res(num + 1, 0);
        int offset = 1;
        res[0] = 0;
        res[1] = 1;

        for (int i = 2; i <= num; ++i) {
            if (!(i & (i - 1))) {
                offset <<= 1;
            }
            res[i] = res[i - offset] + 1;
        }

        return res;
    }
};

int main() {
    Solution sol;
    int n;
    cin >> n;
    vector<int> res = sol.countBits(n);
    for (int i = 0; i < n + 1; ++i) {
        cout << res[i] << " ";
    }
    cout << endl;

    return 0;
}
