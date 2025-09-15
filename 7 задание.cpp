#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;
    
    if (s.size() != 6) {
        cout << "No";
        return 0;
    }
    
    if (s[0] >= 'A' && s[0] <= 'Z' &&
        s[1] >= '0' && s[1] <= '9' &&
        s[2] >= '0' && s[2] <= '9' &&
        s[3] >= '0' && s[3] <= '9' &&
        s[4] >= 'A' && s[4] <= 'Z' &&
        s[5] >= 'A' && s[5] <= 'Z') {
        cout << "Yes";
    } else {
        cout << "No";
    }
}