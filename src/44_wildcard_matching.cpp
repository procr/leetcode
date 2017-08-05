#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
    public:
        bool isMatch(string s, string p) {
            int ls = s.length();
            int lp = p.length();
            vector< vector<bool> > f(ls + 1, vector<bool>(lp + 1, false));
            f[0][0] = true;
            for (int i = 1; i <= ls; ++i) {
                f[i][0] = false;
            }
            for (int j = 1; j <= lp; ++j) {
                if (p[j - 1] == '*') {
                    f[0][j] = f[0][j - 1];
                } else {
                    f[0][j] = false;
                }
            }

            for (int i = 1; i <= ls; ++i) {
                for (int j = 1; j <= lp; ++j) {
                    if (p[j - 1] == '?' || s[i - 1] == p[j - 1]) {
                        f[i][j] = f[i - 1][j - 1];
                    } else if (p[j - 1] == '*') {
                        f[i][j] = f[i - 1][j] | f[i - 1][j - 1] | f[i][j - 1];
                    } 
                }
            }

            return f[ls][lp];
        }

};

int main() {
    Solution sol;
    string s, p;
    cin >> s >> p;
    cout << sol.isMatch(s, p) << endl;
    return 0;
}
