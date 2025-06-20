#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    cout << "Enter the height of the pyramid" << " ";
    int N;
    cin >> N;
    vector<vector<int>> p(N), dp(N);

    for (int i = 0; i < N; i++) {
        p[i].resize(i + 1); dp[i].resize(i + 1);
        for (int j = 0; j <= i; j++) {
            cout << (p[i][j] = dp[i][j] = rand() % 101) << " ";
        }
        cout << endl;
    }

    for (int i = N - 2; i >= 0; i--)
        for (int j = 0; j <= i; j++)
            dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1]);

    cout << "\n" << dp[0][0] << "\n" << p[0][0] << " ";
    for (int i = 1, j = 0; i < N; i++) {
        j = (dp[i][j] < dp[i][j + 1]) ? j : j + 1;
        cout << p[i][j] << " ";
    }
}
