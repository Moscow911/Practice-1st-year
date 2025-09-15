#include <iostream>
using namespace std;

int main() {
    int h, w;
    cin >> h >> w;
    
    int min_r = h, max_r = -1;
    int min_c = w, max_c = -1;
    
    for (int i = 0; i < h; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < w; j++) {
            if (s[j] == '1') {
                if (i < min_r) min_r = i;
                if (i > max_r) max_r = i;
                if (j < min_c) min_c = j;
                if (j > max_c) max_c = j;
            }
        }
    }
    
    cout << min_r << " " << min_c << " " << max_r << " " << max_c;
}