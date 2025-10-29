//Problem 2 (Stack)
//Program: Balanced Parentheses using Stack

 
#include <iostream>
#include <stack>
#include <string>
using namespace std;
 
// Function to check if parentheses are balanced
bool isBalanced(string expr) {
    stack<char> s;
 
    for (char ch : expr) {
        if (ch == '(' || ch == '{' || ch == '[') {
            s.push(ch); // Push opening bracket
        } else {
            if (s.empty()) return false; // No matching opening
 
            char top = s.top();
            s.pop();
 
            if ((ch == ')' && top != '(') ||
                (ch == '}' && top != '{') ||
                (ch == ']' && top != '[')) {
                return false; // Mismatch found
            }
        }
    }
 
    return s.empty(); // If stack empty → balanced
}
 
int main() {
    string expr;
    cout << "Enter bracket expression: ";
    cin >> expr;
 
    if (isBalanced(expr))
        cout << "Balanced ✅" << endl;
    else
        cout << "Not Balanced ❌" << endl;
 
    return 0;
}