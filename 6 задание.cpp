#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a, b, x, y;
        cin >> a >> b >> x >> y;
        int pairs = min(a, x) + min(a, y) + min(b, x);
        cout << pairs << " ";
    }
}