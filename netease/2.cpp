#include <iostream>
#include <string>
#include <strstream>
#include <map>

using namespace std;

int gcd(int a, int b) 
{ 
    if (!b) 
        return (a); 
    return gcd(b, a % b); 
} 

int main() {

    int w, x, y, z;

    while (cin >> w >> x >> y >> z) {

        map<string , int >mm;
        map <string, int>::iterator iter;
        int ans = 0;
        mm.clear();
        
        for (int i = w; i <=x; ++i) {
            for (int j = y; j <=z; ++j) {
                int g = gcd(i, j);
                int a = i / g;
                int b = j / g;
                strstream ss;
                string s;
                ss << a << ":" << b;
                ss >> s;

                iter = mm.find(s);
                if(iter == mm.end()) {
                    mm.insert(pair<string, int>(s, 1));
                    ++ans;
                }

            }
        }
        cout << ans << endl;
    }

    return 0;
}
