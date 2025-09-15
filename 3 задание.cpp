#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<long long> arr(n + 1, 0);
    
    while (k--) {
        int t, i, x;
        cin >> t;
        if (t == 1) {
            cin >> i >> x;
            arr[i] += x;
        } else {
            int u, r;
            cin >> u >> r;
            long long sum = 0;
            for (int j = u; j <= r; j++) sum += arr[j];
            cout << sum << endl;
        }
    }
}