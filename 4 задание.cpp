#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> p(n);
    for (int i = 0; i < n; i++) {
        cin >> p[i];
        p[i]--;
    }
    
    string s;
    cin >> s;
    
    vector<int> cycle(n);
    for (int i = 0; i < n; i++) {
        int pos = i;
        for (int j = 0; j < k % n; j++) {
            pos = p[pos];
        }
        cycle[pos] = i;
    }
    
    string res(n, ' ');
    for (int i = 0; i < n; i++) {
        res[cycle[i]] = s[i];
    }
    
    cout << res << endl;
}