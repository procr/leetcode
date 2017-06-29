#include <iostream>
#include <vector>

using namespace std;

int main() {

    int n;
    vector<int> weight(1, 0);  
    vector<int> val(1, 0); 
    int cap_all = 0;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        int w;
        cin >> w;
        w = w >> 10;
        cap_all += w;
        weight.push_back(w);
        val.push_back(w);
    }

    int cap = cap_all >> 1;

    vector< vector<int> > f(n + 1, vector<int>(cap + 1, 0));
    int max = 0;
    int total = 0;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= cap; ++j) {
            if (weight[i] > j)
            {  
                f[i][j] = f[i - 1][j]; // give up i-th 
            }  
            else if (j >= weight[i]) 
            {  
                int a = f[i - 1][j - weight[i]] + val[i]; // take i-th
                int b = f[i - 1][j]; // give up i-th
                f[i][j] = a > b ? a : b;
            }  
            if (f[i][j] > max) {
                max = f[i][j];
                total = j;
            }
        }
    }

    // cout << cap_all << endl;
    // cout << cap << endl;
    // cout << total << endl;
    cout << ((cap_all - total) << 10) << endl;

    return 0;
}
