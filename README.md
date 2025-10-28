# 🚗 DSA Assignment – Problem 1 (Array): CARVANS – CodeChef ✅
 
---
 
## 📌 Problem Description
Cars are moving in a single lane.  
A car cannot go faster than the car in front of it.  
We need to count how many cars can maintain proper speed.
 
---
 
## 📥 Input Format
T -> number of test cases
M -> number of cars
Speeds -> space separated integers

---
 
## 📤 Expected Output
Print number of cars maintaining valid speed per test case.
3
---
 
## 🧩 Sample Input
3 3 10 7 6 5 10 10 10 10 10 4 8 3 6 11

### ✅ Output
3 5 2

# ----------------------------------------------------------
# CodeChef Problem: CARVANS
# Concept: Array traversal and speed comparison
# ----------------------------------------------------------
 
# Input: Number of test cases
t = int(input("Enter number of test cases: "))
 
for _ in range(t):
    # Input: Number of cars
    n = int(input("\nEnter number of cars: "))
 
    # Input: Speeds of each car separated by spaces
    speeds = list(map(int, input("Enter speeds of cars: ").split()))
 
    # If speeds entered are LESS than number of cars → ERROR
    if len(speeds) != n:
        print("⚠️ Please enter exactly", n, "speeds!")
        continue  # skip this test case
 
    count = 1  # First car always maintains speed
 
    for i in range(1, n):
        if speeds[i] > speeds[i - 1]:
            speeds[i] = speeds[i - 1]
        else:
            count += 1
 
    print("✅ Number of cars maintaining speed:", count)






# ✅ DSA Assignment – Problem 2 (Stack)
 
## 🔹 Topic: Balanced Parentheses using Stack
 
### 📘 Description
This program checks whether the given bracket expression is **balanced** using the **Stack** data structure.  
Brackets must be properly opened and closed in correct order.
 
Example of Balanced ✅:
{[()]}

Example of Not Balanced ❌:
{[(])}

---
 
### 📥 Input Format
- A single string containing only brackets: `() {} []`
 
---
 
### 📤 Output Format
- Print **Balanced ✅** if brackets are properly nested
- Print **Not Balanced ❌** if mismatch occurs
 
---
 
### ✅ Sample Input / Output
| Input | Output |
|-------|--------|
| `{[()]}` | Balanced ✅ |
| `{[(])}` | Not Balanced ❌ |
 
---
 
### 🧠 Algorithm
1️⃣ Traverse each character  
2️⃣ Push opening brackets → Stack  
3️⃣ For closing brackets → check last pushed item  
4️⃣ If mismatch → return Not Balanced  
5️⃣ If stack empty at end → return Balanced ✅  
 
---
 
### 🧑‍💻 Code Screenshot
📌 `/screenshots/problem2_code.png`
 
### 🖥 Output Screenshot
📌 `/screenshots/problem2_output.png`
 
---
 
### 🧰 Tools Used
- Python 3
- VS Code
 
---
 
### 👤 Submitted By
**Sanidhya Singh Sisodiya**  
MBA Tech – Computer Engineering  
Roll No: N252
 
    
