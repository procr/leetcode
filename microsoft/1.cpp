#include <iostream>
#include <vector>
#include <map>
#include <numeric>
#include <limits>

using namespace std;

int main() {
    int P, Q, N;
    while (cin >> P >> Q >> N) {
      float ans;

      float lastIterExpect = 0;

      for (int i = 0; i < N; ++i) {
        ans = 0;
        int step = 1;
        float lastRight = 1;
        int curP = P >> (N - 1 - i);
        while (true) {
          ans += lastRight * (curP / 100.0) * (step + lastIterExpect);
          lastRight *= (1 - curP / 100.0);
          if (curP >= 100)
            break;
          curP = min(100, curP + Q);
          step += 1;
        }
        lastIterExpect = ans;
      }
      printf("%.2f\n", ans);
    }

    return 0;

}