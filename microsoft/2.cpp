#include <iostream>
#include <vector>

using namespace std;

int main() {

    int n, m, k;

    while (cin >> n >> m >> k) {

        vector< int > num_nodes_in_depth(m, 0);

        for (int i = 0; i < m; ++i) {
            cin >> num_nodes_in_depth[i];
        }

        vector< vector<int> > nodes_in_depth(n + 1, vector<int>(n + 1, 0));

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < num_nodes_in_depth[i]; ++j) {
                cin >> nodes_in_depth[i][j];
            }
        }


        vector< int > is_leaves(n + 1, 0);
        vector< int > leaves(k, 0);

        for (int i = 0; i < k; ++i) {
            cin >> leaves[i];
            is_leaves[leaves[i]] = 1;
        }


        vector< vector<int> > dist(n + 1, vector<int>(n + 1, -1));

        for (int i = 0; i < k; ++i) {
            for (int j = 0; j < k; ++j) {
                cin >> dist[leaves[i]][leaves[j]];
            }
        }


        // main function starts here

        vector< int > father(n + 1, 0);

        for (int i = m - 1; i >= 0; --i) {
            int cur_father = -1;
            int last_father_index = 0;
            int need_next_father = 0;
            int last_bro = -1;
            for (int j = 0; j < num_nodes_in_depth[i]; ++j) {

                if (last_bro == -1 || dist[last_bro][nodes_in_depth[i][j]] != 2) {
                    need_next_father = 1;
                }

                // find next fahter
                if (need_next_father) {
                    if (i == 0) {
                        cur_father = 0;
                    } else {
                        for (int t = last_father_index; t < num_nodes_in_depth[i - 1]; ++t) {
                            if (!is_leaves[nodes_in_depth[i - 1][t]]) {
                                cur_father = nodes_in_depth[i - 1][t];
                                last_father_index = t;
                                break;
                            }

                            if (cur_father == -1) {
                                cout << "bad" << endl;
                            }
                        }
                    }
                    need_next_father = 0;
                }

                father[nodes_in_depth[i][j]] = cur_father;
                last_bro = nodes_in_depth[i][j];

                //cout << "level: " << i << " node: " << nodes_in_depth[i][j] << " father: " << cur_father << endl;

                // add new father to leaf
                if(!is_leaves[cur_father]) {

                    // add to map
                    for (int ii = 1; ii <= n; ++ii) {
                        if (is_leaves[ii]) {
                            dist[ii][cur_father] = dist[ii][last_bro] - 1;
                            dist[cur_father][ii] = dist[ii][last_bro] - 1;
                        }
                    }

                    is_leaves[cur_father] = 1;
                }
            }
        }

        for (int i = 1; i <= n - 1; ++i) {
            cout << father[i] << " ";
        }

        cout << father[n] << endl;
        
    }

    return 0;
}
