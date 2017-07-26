#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        int uniquePaths(int m, int n) {
            vector< vector<int> > f(m + 1, vector<int>(n + 1, 0));
            for (int i = 0; i <= m; ++i) {
                f[i][0] = 0;
            }
            for (int j = 0; j <= n; ++j) {
                f[0][j] = 0;
            }
            f[1][1] = 1;
            for (int i = 1; i <= m; ++i) {
                for (int j = 1; j <= n; ++j) {
                    cout << i << j << endl;
                    f[i][j] += (f[i - 1][j] + f[i][j - 1]);
                }
            }
            return f[m][n];
        }
};

int main() {
    Solution sol;
    int m, n;
    cin >> m >> n;
    cout << sol.uniquePaths(m, n) << endl;

    return 0;
}
