#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    int ans = 0;
    cin >> n;
    vector<int> a(n, 0);
    vector<int> b(n, 0);
    for (int i = 0; i < 2 * n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < 2 * n; i++) {
        cin >> b[i];
    }

    for (int i = 0; i < n; i++) {
        ans += (a[i] + b[i + 1]);
    }

    cout << ans << endl;

    return 0;
}
