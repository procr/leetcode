#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        int uniquePathsWithObstacles(vector< vector<int> > & obstacleGrid) {
            int m = obstacleGrid.size();
            int n = 0;
            if (m != 0) {
                n = obstacleGrid[0].size();
            }

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
                    if (obstacleGrid[i - 1][j - 1] == 1) {
                        f[i][j] = 0;
                    } else {
                        f[i][j] += (f[i - 1][j] + f[i][j - 1]);
                    }
                }
            }
            return f[m][n];
        }
};

int main() {
    Solution sol;
    vector< vector<int> > obstacleGrid(3, vector<int>(3, 0));
    obstacleGrid[0][0] = 0;
    obstacleGrid[0][1] = 0;
    obstacleGrid[0][2] = 0;
    obstacleGrid[1][0] = 0;
    obstacleGrid[1][1] = 1;
    obstacleGrid[1][2] = 0;
    obstacleGrid[2][0] = 0;
    obstacleGrid[2][1] = 0;
    obstacleGrid[2][2] = 0;
    cout << sol.uniquePathsWithObstacles(obstacleGrid) << endl;

    return 0;
}
