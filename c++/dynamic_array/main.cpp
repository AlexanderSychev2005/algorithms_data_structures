#include <iostream>
#include <vector>

using namespace std;

int main() {
    // vector<double> digits = {1.0, 2.0, 3.0};
    //
    // digits.reserve(20);
    //
    // digits.push_back(5.0);
    // digits.push_back(4.0);
    // digits.push_back(2.0);
    // digits.push_back(1.0);
    // cout << "Size: " << digits.size() << endl;
    // cout << "Physical size: " << digits.capacity() << endl;
    //
    // // cout << digits[0] << endl;
    // digits[0] = -5;
    // // cout << digits[0] << endl;
    //
    // for (int i=0; i < digits.size(); ++i) {
    //     cout << digits[i] << " ";
    // }

    vector<double> digits(10, 1.0);
    for (int i=0; i < digits.size(); ++i) {
        cout << digits[i] << " ";
    }
    cout << endl;
    digits.pop_back();
    for (int i=0; i < digits.size(); ++i) {
        cout << digits[i] << " ";
    }
    cout << endl;
    digits.clear();
    for (int i=0; i < digits.size(); ++i) {
        cout << digits[i] << " ";
    }

    return 0; 
}