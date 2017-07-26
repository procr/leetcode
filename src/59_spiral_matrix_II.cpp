#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        vector< vector<int> > generateMatrix(int n) {
            vector <vector<int> > matrix(n, vector<int>(n, 0));

            // 0: ->, 1: down, 2: <-, 3: up
            int dir = 0;

            //int top = 0, bottom = n, left = 0, right = n;
            int bound[4] = {-1, n, n, -1};

            int i = 0, j = 0;
            int c = 1;

            int *cur;
            int *next_cur;
            int step;
            int next_step;
            int shrink;

            int total = n * n;

            while (c <= total) {
                cout << i << " " << j << " : " << c << endl;
                matrix[i][j] = c++;
                switch (dir) {
                    case 0: cur = &j; next_cur = &i; step = 1; next_step = 1; shrink = 1; break;
                    case 1: cur = &i; next_cur = &j; step = 1; next_step = -1; shrink = -1; break;
                    case 2: cur = &j; next_cur = &i; step = -1; next_step = -1; shrink = -1; break;
                    case 3: cur = &i; next_cur = &j; step = -1; next_step = 1; shrink = 1; break;
                    default: cout << "!!!\n";
                }
                if (*cur + step != bound[(dir + 1) % 4]) {
                    *cur += step;
                } else {
                    bound[dir] += shrink;
                    dir = (dir + 1) % 4;
                    *next_cur += next_step;
                    
                }
            }
            return matrix;
        }
};

int main() {
    Solution sol;
    int n;
    cin >> n;
    vector< vector<int> > matrix = sol.generateMatrix(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << matrix[i][j];
        }
        cout << endl;
    }

    return 0;
}
