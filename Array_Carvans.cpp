// Problem 1 (Array)
// Program: CARVANS (CodeChef)

 
#include <iostream>
using namespace std;
 
int main() {
    int t;
    cin >> t; // Number of test cases
 
    while (t--) {
        int n;
        cin >> n; // Number of cars
 
        int speed[n];
        for (int i = 0; i < n; i++) {
            cin >> speed[i];
        }
 
        int count = 1; // The first car is always moving at max allowed speed
        int min_speed = speed[0];
 
        for (int i = 1; i < n; i++) {
            if (speed[i] <= min_speed) {
                count++;
                min_speed = speed[i];
            }
        }
 
        cout << count << endl;
    }
 
    return 0;
}